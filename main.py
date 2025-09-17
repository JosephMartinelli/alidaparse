from alidaparse.input import InParam

if __name__ == "__main__":
    show_plots = InParam.from_cli(name="show_plots", required=True, param_type=bool)
    print(show_plots)
