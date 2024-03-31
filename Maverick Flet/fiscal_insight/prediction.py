from flet import *
import requests
from prices.mav_prices import USTECH100, US30, GER40


class Tab_menu(UserControl):
    def __init__(self):
        super().__init__()

        # Event handler for the "GET_APP" icon

    def tabs(self):
        return Container(
            # alignment=alignment.center,
            width=400,
            height=640,
            # bgcolor=colors.ERROR_CONTAINER,
            content=Tabs(
                selected_index=2,
                animation_duration=300,
                divider_color=colors.with_opacity(0.01, 'GREEN900'),
                tab_alignment=TabAlignment.CENTER,
                # overlay_color=colors.RED_900,
                tabs=[
                    Tab(
                        text="GERMAN40",
                        content=Container(
                            content=Container(
                                bgcolor=colors.with_opacity(0.07, 'INDIGO'),
                                # max_extent=200,
                                alignment=alignment.center,
                                animate_offset=300,
                                padding=20,
                                content=Column(
                                    controls=[
                                        Container(
                                            width=400,
                                            height=30,
                                            # bgcolor=colors.TEAL_900,
                                            alignment=alignment.center,
                                            content=Text('GERMAN40', font_family='mm', size=20),

                                        ),
                                        GER40(page),
                                    ]
                                )
                            ),
                            alignment=alignment.center,
                        )
                    ),
                    Tab(
                        text="US30",
                        content=Container(
                            content=Container(
                                bgcolor=colors.with_opacity(0.07, 'INDIGO'),
                                # max_extent=200,
                                alignment=alignment.center,
                                animate_offset=300,
                                padding=20,
                                content=Column(
                                    controls=[
                                        Container(
                                            width=400,
                                            height=30,
                                            # bgcolor=colors.TEAL_900,
                                            alignment=alignment.center,
                                            content=Text('US30', font_family='mm', size=20),

                                        ),
                                        US30(page),
                                    ]
                                )
                            ),
                            alignment=alignment.center,
                        )
                    ),
                    Tab(
                        text="NASDAQ100",
                        content=Container(
                            content=Container(
                                bgcolor=colors.with_opacity(0.07, 'INDIGO'),
                                # max_extent=200,
                                alignment=alignment.center,
                                animate_offset=300,
                                padding=20,
                                content=Column(
                                    controls=[
                                        Container(
                                            width=400,
                                            height=30,
                                            # bgcolor=colors.TEAL_900,
                                            alignment=alignment.center,
                                            content=Text('NASDAQ100', font_family='mm', size=20),

                                        ),
                                        USTECH100(page),
                                    ]
                                )
                            ),
                            alignment=alignment.center,
                        )
                    ),
                    # Tab(
                    #     text="DXY",
                    #     content=Container(
                    #         content=Container(
                    #             bgcolor=colors.with_opacity(0.07, 'INDIGO'),
                    #             # max_extent=200,
                    #             alignment=alignment.center,
                    #             animate_offset=300,
                    #             padding=20,
                    #             content=Stack(
                    #                 controls=[
                    #                     Icon(icons.LEADERBOARD, size=100, opacity=0.5),
                    #                 ]
                    #             )
                    #         )
                    #     )
                    # ),
                    # Tab(
                    #     text="JPY",
                    #     # icon=icons.SETTINGS,
                    #     content=Container(
                    #         content=Container(
                    #             bgcolor=colors.with_opacity(0.07, 'INDIGO'),
                    #             # max_extent=200,
                    #             alignment=alignment.center,
                    #             animate_offset=300,
                    #             padding=20,
                    #             content=Stack(
                    #                 controls=[
                    #                     Icon(icons.LEADERBOARD, size=100, opacity=0.5),
                    #
                    #                 ]
                    #             )
                    #         )
                    #     )
                    # ),
                ],
                expand=1,
            )
        )

    def build(self):
        return self.tabs()
