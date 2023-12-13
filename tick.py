 permission = 2

tick = {

    'N': '\u00A7a tick加速已经关闭',

    'Y': '\u00A7c tick加速已经开始',

    'fy': 'freeze已 \u00A7c 关闭',

    'fn': 'freeze已 \u00A7a 开启'

}

help_msg = '''========== MCDR-tick v1.0 ==========

!!tick Y / Yes   开启加速

!!tick N / No   关闭加速

!!tick f / freeze 开启/关闭 freeze

'''

global_tick_count = 0



def on_info(server, info):

    global global_tick_count



    if info.content.startswith('!!tick'):

        args = info.content.split()

        if len(args) == 1:

            server.say(help_msg)

        elif args[1] == 'Yes' or args[1] == 'Y':

            if len(args) == 2:

                server.execute('/tick rate 200')

                server.execute('/title @a title [{"text":"tick 加速已经开始 小心！！","color":"gold","bold":true,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')

                server.say(tick['Y'])

        elif args[1] == 'No' or args[1] == 'N':

            if len(args) == 2:

                server.execute('/tick rate 20')

                server.execute('/title @a title [{"text":"tick 加速已经关闭！！","color":"gold","bold":true,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')

                server.say(tick['N'])

        elif args[1] == 'freeze' or args[1] == 'f':

            if len(args) == 2:

                server.execute('/tick freeze')

                global_tick_count += 1

                if global_tick_count % 2 == 1:

                    server.say(tick['fn'])

                else:

                    server.say(tick['fy'])

        elif args[1] == 'help':

            if len(args) == 2:

                server.say(help_msg)

