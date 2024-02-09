from shiny import render, App, ui
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ui.include_css(Path(__file__).parent /"style.css")

app_ui = ui.page_fluid(
    ui.h1("Data visualiser"),
    ui.row(
        ui.column(2, ui.h5("Enter Number: ")),
        ui.column(10,ui.input_numeric("random_num", "","3"))
    ),
    # ui.row(
    #     ui.column(1, ui.h5("Enter URL: ")),
    #     ui.column(11,ui.input_text_area("url", "","https://restcountries.com/v3.1/all?fields=name,postalCode"))
    # ),
    # ui.input_text("in_name", "Enter name", "John"),
    # ui.output_text("display_name"),
    ui.output_plot("show_plot"),
)

def server(input, output, session):
    
    @output
    @render.plot
    def show_plot():
        np.random.seed(19680801)
        x_rand = 100 + 15 * np.random.randn(437)
        fig, ax = plt.subplots()
        ax.hist(x_rand, int(input.random_num()), density=True)
        return fig

    

    @output
    @render.text
    def display_name():
        return f"name entered is {input.in_name()}"
    

app = App(app_ui, server)
