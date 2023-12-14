from ctypes import ArgumentError
from turtle import hideturtle


permission = 2
tick = {
    'aclr': 'tick加速已经 \u00A7a 开始',
    'def': 'tick加速已经 \u00A7c 关闭',
    'fy': 'freeze已 \u00A7c 关闭',
    'fn': 'freeze已 \u00A7a 开启',
    'r': '\u00A7a tick 已经被 \u00A76 {} \u00A7a 设置为 \u00A7c {}'
}
help_msg = '''
========== MCDR-tick v1.4 ==========
\u00A7f !!tick help / h              \u00A77 查看帮助
\u00A7f !!tick accelerate / aclr   \u00A77 满tick加速
\u00A7f !!tick default / def     \u00A77 恢复默认tick
\u00A7f !!tick freeze / frz  \u00A77 开启/关闭 freeze
\u00A7f !!tick rate / r        \u00A77 自定义tick速度
'''

global_tick_count = 0

def on_info(server, info):
    global global_tick_count
    name = info.player
    args = info.content.split()
    if info.content.startswith('!!tick'):
        if len(args) == 1:
            server.say(help_msg)
        elif args[1] == 'accelerate' or args[1] == 'aclr':
            if len(args) == 2:
                server.execute('/tick rate 500')
                server.execute('/title @a title [{"text":"tick 加速已经开始！！","color":"gold","bold":true,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                server.say(tick['aclr'])
        elif args[1] == 'default' or args[1] == 'def':
            if len(args) == 2:
                server.execute('/tick rate 20')
                server.execute('/title @a title [{"text":"tick 加速已经关闭！！","color":"gold","bold":true,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false}]')
                server.say(tick['def'])
        elif args[1] == 'freeze' or args[1] == 'frz':
            if len(args) == 2:
                server.execute('/tick freeze')
                global_tick_count += 1
                if global_tick_count % 2 == 1:
                    server.say(tick['fn'])
                else:
                    server.say(tick['fy'])
        elif args[1] == 'rate' or args[1] == 'r':      
            if len(args) == 3:
                tick_rate_value = args[2]
                server.execute('/tick rate {}'.format(tick_rate_value))
                server.say(tick['r'].format(name,tick_rate_value))
        elif args[1] == 'help' or args[1] == 'h':
            if len(args) == 2:
                server.tell(name,help_msg)
