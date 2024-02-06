from shiny import render, App, ui

app_ui = ui.page_fluid(
    ui.input_text("in_name", "Enter name", "John"),
    ui.output_text("display_name")
)

def server(input, output, session):
    
    @output
    @render.text
    def display_name():
        return f"name entered is {input.in_name()}"
    

app = App(app_ui, server)
