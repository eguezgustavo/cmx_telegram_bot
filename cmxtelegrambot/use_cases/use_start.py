import collections
import typing

from cmxtelegrambot.core.entities.command import Command

CommandDescription = collections.namedtuple('CommandDescription', ['name', 'description'])


def use_start(title: str, commands: typing.List[CommandDescription], register_command, dispatcher, authentication_service):
    def on_start(command: Command):
        response = title + '\n\n'
        response += '\n'.join([f'/{c.name}: {c.description}' for c in commands])
        command.reply(response)        


    register_command('start', dispatcher, authentication_service, on_start)
