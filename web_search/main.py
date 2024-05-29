from duckduckgo_search import DDGS
from trafilatura import fetch_url, extract
from api.interface import (
    SettingsConfig,
    SkillConfig,
    WingmanConfig,
    WingmanInitializationError,
)
from api.enums import LogType
from skills.skill_base import Skill


class WebSearch(Skill):

    def __init__(
        self,
        config: SkillConfig,
        wingman_config: WingmanConfig,
        settings: SettingsConfig,
    ) -> None:
        super().__init__(
            config=config, wingman_config=wingman_config, settings=settings
        )

    async def validate(self) -> list[WingmanInitializationError]:
        errors = await super().validate()
        return errors

    def get_tools(self) -> list[tuple[str, dict]]:
        tools = [
            (
                "web_search_function",
                {
                    "type": "function",
                    "function": {
                        "name": "web_search_function",
                        "description": "Searches the internet / web for the topic identified by the user or identified by the AI in order to answer a user question.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "search_query": {
                                    "type": "string",
                                    "description": "The topic to search the internet for.",
                                },
                                "search_type": {
                                    "type": "string",
                                    "description": "The type of search the user wants to perform, default to 'news', but use 'general' if the user is not looking for current events, weather, or date information.  If it is not clear what type of search the user wants, ask.",
                                    "enum": [
                                        "news",
                                        "general",
                                    ],
                                },
                            },
                            "required": ["search_query", "search_type"],
                        },
                    },
                },
            ),
        ]
        return tools

    async def execute_tool(
        self, tool_name: str, parameters: dict[str, any]
    ) -> tuple[str, str]:
        function_response = "No search results found or search failed."
        instant_response = ""

        if tool_name == "web_search_function":
            if self.settings.debug_mode:
                self.start_execution_benchmark()
                await self.printr.print_async(
                    f"Executing web_search_function with parameters: {parameters}",
                    color=LogType.INFO,
                )
            final_results = ""
            search_query = parameters.get("search_query")
            search_type = parameters.get("search_type")

            if search_type == "general":
                search_results = DDGS().text(search_query, safesearch="off", max_results=5)
            else:
                search_results = DDGS().news(search_query, safesearch="off", max_results=5)

            for result in search_results:
                title = result.get("title")
                link = result.get("url")
                if search_type == "general":
                    link = result.get("href")
                body = result.get("body")
                if link:
                    trafilatura_url = link
                    trafilatura_downloaded = fetch_url(trafilatura_url)
                    trafilatura_result = extract(trafilatura_downloaded, include_comments=False, include_tables=False)#, no_fallback=True, favor_precision=True)
                    if trafilatura_result:
                        final_results = final_results + "\n" + title + "\n" + link + "\n" + trafilatura_result[:2000] + "\n\n"
                        if self.settings.debug_mode:
                            await self.printr.print_async(
                                f"web_search skill analyzing website at: {link} for full content using trafilatura",
                                color=LogType.INFO,
                            )
                    else:
                        final_results = final_results + "\n" + title + "\n" + link + "\n" + body + "\n\n"
                else:
                    final_results = final_results + "\n" + title + "\n" + body + "\n\n"

            if final_results != "":
                if self.settings.debug_mode:
                    await self.printr.print_async(
                        f"Final web_search skill results used as context for AI response: \n\n {final_results}",
                        color=LogType.INFO,
                    )
                function_response = final_results

            if self.settings.debug_mode:
                await self.print_execution_time()

        return function_response, instant_response

