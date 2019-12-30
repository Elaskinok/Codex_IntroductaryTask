import logging
from command_executor import CommandExecutor

INPUT_FNAME = 'input.txt'
OUTPUT_FNAME = 'output.txt'


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    try:
        with open(INPUT_FNAME, mode='r') as file:
            commands = file.read().split('\n')
    except FileNotFoundError:
        logging.warning("File 'input.txt' does not exist !")

    cmd_executor = CommandExecutor()

    with open(OUTPUT_FNAME, mode='w') as file:
        for command in commands[:-1]:
            if cmd_executor.execute_command(command):
                file.write(cmd_executor.get_canvas_as_string())
                file.write('\n')

                logging.info(f'{command}' + ' - success')
