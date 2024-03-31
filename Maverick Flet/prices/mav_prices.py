import requests
from flet import *


class USTECH100(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.open_field = TextField(label="Open Price", border_color=colors.WHITE)
        self.volume_field = TextField(label="Volume", border_color=colors.WHITE)
        self.low_field = TextField(label="Low Price", border_color=colors.WHITE)
        self.high_field = TextField(label="High Price", border_color=colors.WHITE)

        self.button_add = IconButton(icons.GET_APP, on_click=self.add_hello)
        self.button_clear = IconButton(icons.DELETE_FOREVER, on_click=self.clear_textfield)
        self.button_disabled = IconButton(icons.REMOVE_OUTLINED, disabled=True)
        self.button_refresh = IconButton(icons.AUTORENEW_OUTLINED, on_click=self.add_hello)
        self.button_submit = IconButton(icons.SEND, on_click=self.button_submit)
        self.pred_container = Container(
            alignment=alignment.center,
            width=400,
            height=150,
            # bgcolor=colors.BLUE_900,
            border=border.all(1.50, colors.BLUE_GREY_900),
            border_radius=10,
            content=Text(value="Results", size=14, font_family="mm", weight='bold'),

        )

    def add_hello(self, e):
        data = requests.get("https://index-i.onrender.com/nasdaq").text
        open_price = data.split("Open: ")[1].split("\\n")[0]
        volume = data.split("Volume: ")[1].split("\\n")[0]
        low = data.split("Daily Low: ")[1].split("\\n")[0]
        high = data.split("Daily High: ")[1].split("\\n")[0]

        self.low_field.value = low
        self.high_field.value = high
        self.volume_field.value = volume
        self.open_field.value = open_price
        self.update()

    def clear_textfield(self, e):
        self.open_field.value = ""
        self.volume_field.value = ""
        self.low_field.value = ""
        self.high_field.value = ""
        self.pred_container.content = Text(value="Results", size=14, font_family="mm", weight='bold')
        self.update()

    def button_submit(self, e):
        data = {key: float(getattr(self, f"{key}_field").value.replace(',', '')) for key in
                ["open", "volume", "low", "high"]}
        response = requests.post("https://index-i.onrender.com/nas100", json=data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            self.output_data(prediction)
            print(f"Data posted successfully! Prediction: {prediction}")
        else:
            print(f"Failed to post data. Response: {response.text}")

    def output_data(self, data):
        # Update the content of pred_container with the posted data
        self.pred_container.content = Text(value=str(data), size=14, font_family="mm", weight='bold')
        self.update()

    def build(self):
        return Column([
            self.open_field,
            self.volume_field,
            self.low_field,
            self.high_field,
            Row(
                alignment=MainAxisAlignment.CENTER,
                height=80,
                spacing=20,
                # width=300,
                controls=[
                    Container(
                        bgcolor=colors.BLUE_900,
                        border_radius=5,
                        padding=5,
                        # height=70,
                        content=Row(
                            expand=4,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                self.button_add,
                                self.button_clear,
                                self.button_disabled,
                                self.button_refresh,
                                self.button_submit,
                            ]),
                    ),
                ],
            ),
            self.pred_container,
        ])

    # TODO change to GBPJPY to US30 for now


class US30(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.open_field = TextField(label="Open Price", border_color=colors.WHITE)
        self.volume_field = TextField(label="Volume", border_color=colors.WHITE)
        self.low_field = TextField(label="Low Price", border_color=colors.WHITE)
        self.high_field = TextField(label="High Price", border_color=colors.WHITE)

        self.button_add = IconButton(icons.GET_APP, on_click=self.add_hello)
        self.button_clear = IconButton(icons.DELETE_FOREVER, on_click=self.clear_textfield)
        self.button_disabled = IconButton(icons.REMOVE_OUTLINED, disabled=True)
        self.button_refresh = IconButton(icons.AUTORENEW_OUTLINED, on_click=self.add_hello)
        self.button_submit = IconButton(icons.SEND, on_click=self.button_submit)
        self.pred_container = Container(
            alignment=alignment.center,
            width=400,
            height=150,
            # bgcolor=colors.BLUE_900,
            border=border.all(1.50, colors.BLUE_GREY_900),
            border_radius=10,
            content=Text(value="Results", size=14, font_family="mm", weight='bold'),

        )

    def add_hello(self, e):
        data = requests.get("https://index-i.onrender.com/dowjones").text
        open_price = data.split("Open: ")[1].split("\\n")[0]
        volume = data.split("Volume: ")[1].split("\\n")[0]
        low = data.split("Daily Low: ")[1].split("\\n")[0]
        high = data.split("Daily High: ")[1].split("\\n")[0]

        self.low_field.value = low
        self.high_field.value = high
        self.volume_field.value = volume
        self.open_field.value = open_price
        self.update()

    def clear_textfield(self, e):
        self.open_field.value = ""
        self.volume_field.value = ""
        self.low_field.value = ""
        self.high_field.value = ""
        self.pred_container.content = Text(value="Results", size=14, font_family="mm", weight='bold')
        self.update()

    def button_submit(self, e):
        data = {key: float(getattr(self, f"{key}_field").value.replace(',', '')) for key in
                ["open", "volume", "low", "high"]}
        response = requests.post("https://index-i.onrender.com/us30", json=data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            self.output_data(prediction)
            print(f"Data posted successfully! Prediction: {prediction}")
        else:
            print(f"Failed to post data. Response: {response.text}")

    def output_data(self, data):
        # Update the content of pred_container with the posted data
        self.pred_container.content = Text(value=str(data), size=14, font_family="mm", weight='bold')
        self.update()

    def build(self):
        return Column([
            self.open_field,
            self.volume_field,
            self.low_field,
            self.high_field,
            Row(
                alignment=MainAxisAlignment.CENTER,
                height=80,
                spacing=20,
                # width=300,
                controls=[
                    Container(
                        bgcolor=colors.BLUE_900,
                        border_radius=5,
                        padding=5,
                        # height=70,
                        content=Row(
                            expand=4,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                self.button_add,
                                self.button_clear,
                                self.button_disabled,
                                self.button_refresh,
                                self.button_submit,

                            ]),
                    ),
                ],
            ),
            self.pred_container,
        ])
#
#     # TODO change to GOLD to GERMAN40 for now
#
class GER40(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.open_field = TextField(label="Open Price", border_color=colors.WHITE)
        self.volume_field = TextField(label="Volume", border_color=colors.WHITE)
        self.low_field = TextField(label="Low Price", border_color=colors.WHITE)
        self.high_field = TextField(label="High Price", border_color=colors.WHITE)

        self.button_disabled = IconButton(icons.REMOVE_OUTLINED, disabled=True)
        self.button_refresh = IconButton(icons.AUTORENEW_OUTLINED, on_click=self.add_hello)
        self.button_submit = IconButton(icons.SEND, on_click=self.button_submit)
        self.button_add = IconButton(icons.GET_APP, on_click=self.add_hello)
        self.button_clear = IconButton(icons.DELETE_FOREVER, on_click=self.clear_textfield)
        self.pred_container = Container(
            alignment=alignment.center,
            width=400,
            height=150,
            # bgcolor=colors.BLUE_900,
            border=border.all(1.50, colors.BLUE_GREY_900),
            border_radius=10,
            content=Text(value="Results", size=14, font_family="mm", weight='bold'),

        )

    def add_hello(self, e):
        data = requests.get("https://index-i.onrender.com/german40").text
        open_price = data.split("Open: ")[1].split("\\n")[0]
        volume = data.split("Volume: ")[1].split("\\n")[0]
        low = data.split("Daily Low: ")[1].split("\\n")[0]
        high = data.split("Daily High: ")[1].split("\\n")[0]

        self.low_field.value = low
        self.high_field.value = high
        self.volume_field.value = volume
        self.open_field.value = open_price
        self.update()

    def clear_textfield(self, e):
        self.open_field.value = ""
        self.volume_field.value = ""
        self.low_field.value = ""
        self.high_field.value = ""
        self.pred_container.content = Text(value="Results", size=14, font_family="mm", weight='bold')
        self.update()

    def button_submit(self, e):
        data = {key: float(getattr(self, f"{key}_field").value.replace(',', '')) for key in
                ["open", "volume", "low", "high"]}
        response = requests.post("https://index-i.onrender.com/ger30", json=data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            self.output_data(prediction)
            print(f"Data posted successfully! Prediction: {prediction}")
        else:
            print(f"Failed to post data. Response: {response.text}")

    def output_data(self, data):
        # Update the content of pred_container with the posted data
        self.pred_container.content = Text(value=str(data), size=14, font_family="mm", weight='bold')
        self.update()

    def build(self):
        return Column([
            self.open_field,
            self.volume_field,
            self.low_field,
            self.high_field,
            Row(
                alignment=MainAxisAlignment.CENTER,
                height=80,
                spacing=20,
                # width=300,
                controls=[
                    Container(
                        bgcolor=colors.BLUE_900,
                        border_radius=5,
                        padding=5,
                        # height=70,
                        content=Row(
                            expand=4,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                self.button_add,
                                self.button_clear,
                                self.button_disabled,
                                self.button_refresh,
                                self.button_submit,

                            ]),
                    ),
                ],
            ),
            self.pred_container,
        ])
