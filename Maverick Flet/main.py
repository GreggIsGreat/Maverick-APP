from flet import *
from sidebar.sidebar import ModernNavBar
from fiscal_insight.prediction import Tab_menu
from barcharts.barchart import Bar_chart


# TODO: Thabang Teddy

# User Controls
class SideNavbar(UserControl):
    pass

    def UserData(self, name: str, description: str):
        return Container(
            content=Row(
                controls=[
                    Column(
                        spacing=3,
                        # alignment=alignment.bottom_left,
                        controls=[
                            Text(
                                value=name,
                                size=12,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200,
                                font_family='mm'
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight=400,
                                color='white54',
                                opacity=1,
                                animate_opacity=200,
                                font_family='mm'
                            ),
                        ]
                    )
                ],
                alignment=MainAxisAlignment.START
            ),
            padding=-10
        )

    def build(self):
        return Container(
            width=50,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
        )


navbar = SideNavbar()


# AppBar Controls
class NavigationPanel(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page  # this had to be moved lower just for it to work!!! Stupid Things fr!!
        self.drawer = NavigationDrawer(
            indicator_shape=None,
            controls=[
                Container(
                    height=200,
                    bgcolor='BLUE900',
                    content=Text("Maverick", size=25, font_family='bl'),
                    margin=10,
                    padding=10,
                    border_radius=10,
                    alignment=alignment.center,
                    on_click=lambda e: print("Clickable without Ink clicked!")
                ),
                ModernNavBar(),
            ]
        )
        self.page.drawer = self.drawer

    def show_drawer(self, e):
        self.drawer.open = True
        self.drawer.update()
        print('Drawer Is Working')

    def account_page(self, e):
        # print(self.page)
        self.page.go('/account')

    def settings_page(self, e):
        self.page.go('/settings')

    def intrinsic_value(self, e):
        self.page.go('/intrinsic')

    def dashboard(self, e):
        self.page.go('/')

    def topnav(self):
        # account_page = menu_item_clicked()
        return AppBar(
            leading=IconButton(icons.MENU_ROUNDED, on_click=self.show_drawer),
            title=navbar.UserData('Thabang Teddy', 'Data Scientist'),  # Big Data Software Developer
            actions=[
                # CircleAvatar(
                #     bgcolor='BLUE800',
                #     color='WHITE',
                #     content=Text('TED', size=12),
                # ),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text='Account', on_click=self.account_page),
                        PopupMenuItem(text='Settings', on_click=self.settings_page),
                    ],
                ),
            ],
            bgcolor='BLUE900'
        )

    def build(self):
        return self.topnav()


class iconSwitch(UserControl):

    def flipSwitch(self, e):
        e.control.selected = not e.control.selected
        # e.control.rotate.angle += 8
        e.control.update()

    def build(self):
        return IconButton(
            icon=icons.TOGGLE_OFF_OUTLINED,
            selected_icon=icons.TOGGLE_ON_ROUNDED,
            on_click=self.flipSwitch,
            selected=False,
            icon_size=35,
            # rotate=transform.Rotate(0, alignment=alignment.center),
            # animate_rotation=animation.Animation(900, AnimationCurve.BOUNCE_OUT),
            style=ButtonStyle(color={"selected": colors.BLUE}),
        )


def main(page: Page) -> None:
    page.title = "Maverick"
    page.window_width = 400  # window's width is 400 px
    page.window_height = 800  # window's height is 800 px
    page.window_resizable = False
    page.theme_mode = ThemeMode.DARK

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.scroll = ScrollMode.AUTO

    top = NavigationPanel(page)
    menu = top.drawer
    switch = iconSwitch()


    page.fonts = {
        'bl': 'fonts/Blanka-Regular.otf',
        'os': 'fonts/Oswald-Regular.otf',
        'mm': 'fonts/MartianMono-Regular.ttf'
    }

    def route_change(e: RouteChangeEvent) -> None:
        # page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    Text(value='MaveRick.', size=50, color='white', font_family='bl'),
                    IconButton(
                        icon=icons.NAVIGATE_NEXT,
                        icon_color="BLUE400",
                        icon_size=40,
                        tooltip="Open",
                        on_click=lambda _: page.go('/mainpage'))],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26,
            ),

        )

        # MainPage View
        if page.route == "/mainpage":
            topnav = top.topnav()
            page.views.append(
                View(
                    route='/mainpage',
                    controls=[
                        topnav,
                        menu,
                        Container(
                            Column([
                                Text(
                                    value='DASHBOARD',
                                    weight='BOLD',
                                    size=25,
                                    text_align='CENTER',
                                    # fonts='os'
                                ),
                                Row([
                                    Text(
                                        value='BALANCE',
                                        size=10,
                                        font_family='mm'
                                        # text_align = 'CENTER', 
                                    ),
                                    Text(
                                        value='P4 000 000.00',
                                        size=12,
                                        weight='BOLD',
                                        font_family='mm'
                                        # text_align = 'CENTER', 
                                    ),
                                    Icon(
                                        icons.TRENDING_UP,
                                        color='GREEN',

                                    ),
                                    # Icon(icons.TRENDING_DOWN,
                                    #      color='red')
                                ]),
                            ],
                                expand=True,
                            ),

                            bgcolor=colors.with_opacity(0.03, 'WHITE54'),
                            padding=10,
                            margin=2,
                            # opacity = 0.1,
                            width=400,
                            height=100,
                            border_radius=10,
                            # border= border.all(
                            #     color='BLUE800',
                            # )
                        ),
                        Container(
                            # bgcolor=colors.with_opacity(0.03, 'WHITE54'),
                            height=70,
                            # margin=-15,
                            padding=10,
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                # alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Row(controls=[
                                        Text('Time Frame:', weight='bold'),
                                        Dropdown(
                                            border=InputBorder.NONE,
                                            bgcolor=None,
                                            content_padding=Padding(top=10, right=10, bottom=10, left=10),
                                            width=140,
                                            hint_text="Select TF",
                                            options=[
                                                dropdown.Option("Daily"),
                                                dropdown.Option("Weekly"),
                                                dropdown.Option("Monthly"),
                                            ],
                                        ),
                                    ]),
                                    Text('Auto:', weight='bold'),
                                    # IconButton(icons.TOGGLE_OFF_OUTLINED, icon_size=35),
                                    switch

                                ])

                        ),
                        Container(
                            # bgcolor=colors.with_opacity(0.03, 'WHITE54'),
                            height=50,
                            padding=10,
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Text('Show:', weight='bold'),
                                    Checkbox(label="Open", value=False, active_color='GREEN'),
                                    Checkbox(label="Close", value=False, active_color='GREEN'),
                                    Checkbox(label="Low", value=False, active_color='GREEN'),
                                    Checkbox(label="High", value=False, active_color='GREEN'),

                                ])

                        ),
                        Card(
                            width=400,
                            height=380,
                            content=Container(
                                alignment=alignment.center,
                                padding=15,
                                content=Bar_chart()
                            )
                        ),

                        # Random additions i like
                        Container(
                            # bgcolor=colors.BLACK26,
                            # height=70,
                            content=Row(
                                expand=4,
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    IconButton(icons.CANDLESTICK_CHART),
                                    IconButton(icons.HISTORY),
                                    IconButton(icons.SEARCH),
                                    IconButton(icons.CLOSE),
                                    IconButton(icons.OPEN_WITH),

                                ])

                        ),
                        #
                        # Container(
                        #     width=400,
                        #     height=40,
                        #     alignment=alignment.center,
                        # ),

                    ]
                )
            )

        # Account View
        if page.route == "/account":
            topnav = top.topnav()
            page.views.append(
                View(
                    route='/account',
                    controls=[
                        topnav,
                        menu,
                        FloatingActionButton(
                            icon=icons.HOME_FILLED,
                            on_click=lambda _: page.go('/mainpage')
                        ),
                        Container(
                            Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Container(
                                        width=200,
                                        padding=10,
                                        alignment=alignment.center_left,
                                        content=Text(
                                            value='PROFILE PAGE',
                                            weight='BOLD',
                                            size=25,
                                        ),
                                    ),
                                    # Container(
                                    #     width=100,
                                    #     padding=10,
                                    #     alignment=alignment.center_right,
                                    #     content=Icon(
                                    #         icons.PERSON,
                                    #         color='BLUE',
                                    #         size=30,
                                    #     ),
                                    # ),
                                ]),
                            # bgcolor=colors.with_opacity(0.03, 'WHITE54'),
                            # padding=8,
                            # margin=2,
                            # width=400,
                            # height=100,
                            # border_radius=10,
                        ),
                        Container(
                            height=500,
                            alignment=alignment.center,
                            content=Icon(
                                icons.PERSON,
                                color=colors.with_opacity(0.4, 'WHITE54'),
                                size=50,
                            ),
                        ),

                    ]
                )
            )
        # Economic View
        if page.route == "/economic":
            topnav = top.topnav()
            page.views.append(
                View(
                    route='/economic',
                    controls=[
                        topnav,
                        menu,
                        FloatingActionButton(
                            icon=icons.HOME_FILLED,
                            on_click=lambda _: page.go('/mainpage')
                        ),
                        Row(
                            controls=[
                                Text(
                                    value='ECONOMIC DATA',
                                    weight='BOLD',
                                    size=25,
                                ),
                                IconButton(
                                    icons.ERROR,
                                    # on_click=lambda _: page.go('/mainpage'),
                                    tooltip="Feature Coming Soon!"
                                )
                            ]
                        ),

                        GridView(
                            expand=1,
                            max_extent=200,
                            animate_offset=300,
                            controls=[
                                # Nonfarm Payrolls
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    border_radius=border_radius.all(10),
                                    content=Column(
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('+410', size=20, weight='bold', color=colors.GREEN)
                                            ),
                                            Text('Nonfarm Payrolls'),

                                        ]),

                                ),
                                # Initial Jobless Claims
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    # bgcolor='#36454F',
                                    border_radius=border_radius.all(10),
                                    # ink=True,
                                    # on_click=lambda e: print("Initial Jobless Claims"),
                                    content=Column(
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('-110', size=20, weight='bold', color=colors.RED)
                                            ),
                                            Text('Initial Jobless Claims'),

                                        ]),

                                ),
                                # Fed Balance Sheet
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    border_radius=border_radius.all(10),
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('-260', size=20, weight='bold', color=colors.RED)
                                            ),
                                            Text('Fed Balance Sheet'),

                                        ]),

                                ),
                                # Unemployment Rate
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    border_radius=border_radius.all(10),
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('+510', size=20, weight='bold', color=colors.GREEN),
                                            ),
                                            Text('Unemployment Rate'),

                                        ]),
                                ),
                                # Another Economic Value
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    border_radius=border_radius.all(10),
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('-', size=20, weight='bold', color=colors.GREEN),
                                            ),
                                            Text('Economic Value'),

                                        ]),
                                ),
                                # Another Economic Value
                                Container(
                                    padding=10,
                                    alignment=alignment.center,
                                    bgcolor=colors.with_opacity(0.4, 'INDIGO'),
                                    border_radius=border_radius.all(10),
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                width=150,
                                                height=120,
                                                bgcolor=colors.BLACK26,
                                                border_radius=border_radius.all(10),
                                                content=Text('-', size=20, weight='bold', color=colors.GREEN),
                                            ),
                                            Text('Economic Value'),

                                        ]),
                                ),
                            ]
                        ),
                        Container(
                            padding=8,
                            content=FloatingActionButton(
                                icon=icons.REPLAY_SHARP,
                                bgcolor=colors.ERROR_CONTAINER,
                                rotate=transform.Rotate(0, alignment=alignment.center),
                                animate_rotation=animation.Animation(900, AnimationCurve.BOUNCE_OUT),
                                # style=ButtonStyle(color={"selected": colors.BLUE, "": colors.WHITE})
                                # on_click=lambda _: page.go('/mainpage')
                            ),
                        )
                    ]
                )
            )

        # Predictor  View
        if page.route == "/predictor":
            topnav = top.topnav()
            page.views.append(
                View(
                    route='/predictor',
                    controls=[
                        topnav,
                        menu,
                        FloatingActionButton(
                            icon=icons.HOME_FILLED,
                            on_click=lambda _: page.go('/mainpage')
                        ),
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Text(
                                    value='FISCAL INSIGHT',
                                    size=25,
                                    weight='bold',
                                    # font_family='os'
                                ),
                                IconButton(icons.HISTORY_SHARP,
                                           tooltip="Feature Coming Soon!")
                            ]),

                        Tab_menu(),
                    ]
                )
            )

        # Settings View
        if page.route == "/settings":
            topnav = top.topnav()
            page.views.append(
                View(
                    route='/settings',
                    controls=[
                        topnav,
                        menu,
                        FloatingActionButton(
                            icon=icons.HOME_FILLED,
                            bgcolor='RED800',
                            on_click=lambda _: page.go('/mainpage')
                        ),
                        Text(
                            value='SETTINGS PAGE',
                            weight='BOLD',
                            size=25,
                            # font_family='MM'
                        ),
                        Container(
                            height=500,
                            alignment=alignment.center,
                            content=Icon(
                                icons.SETTINGS,
                                color=colors.with_opacity(0.4, 'WHITE54'),
                                size=50,
                            ),
                        ),
                    ]
                )
            )

    page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main, assets_dir='assets')
