PLUGIN_METADATA = {
    “id”： “家”，
    “版本”： “1.0.0”，
    “名称”： “家”，
    “作者”： “大太”，
    “依赖关系”：{
        “麦克德锻造”： “<1.0.0”，
    }
}

导入 JSON
导入时间

#帮助信息
help_msg  = '''=-=-= §aMCDR Home插件帮助信息 §f=-=-=
嘭！！主页 帮助 §f- §c显示帮助消息
嘭！！sethome [家名]§f- §c设置家，默认值为home
嘭！！delhome [家名]§f- §c删除家，默认值为home
嘭！！Home [家名]§f- §c传送回家，默认值为home
嘭！！主页列表§f- §c显示已有主页列表
§f=-=-=''

tp_tran = {
    0： '我的世界：主世界'，
    -1： '我的世界：the_nether'，
    1： '我的世界：主世界'，
    “我的世界：主世界”： “我的世界：主世界”，
    “我的世界：the_nether”： “我的世界：the_nether”，
    “我的世界：the_end”： “我的世界：the_end”
}

dim_tran = {
    0： '§a主世界'，
    -1： '§c地狱'，
    1： '§6末地'，
    '我的世界：主世界'： '§a主世界'，
    '我的世界：the_nether'： '§c地狱'，
    “我的世界：the_end”： “§6末地”
}

json_filename = 'config/home.json'

家庭 = {}

def on_info（服务器，信息）：
    如果信息。is_player == 1：
        如果信息。内容。开头为（'！！家'）：
            参数 = 信息。内容。分裂(' ')
            如果 len（args） == 1：
                主页 = “家”
                back_home（信息，服务器，首页)
            Elif len（args） == 2：
                如果参数[1] == '帮助'：
                    服务器。告诉（信息。播放器，help_msg)
                elif args[1] == “list”：
                    print_home（信息，服务器)
                其他：
                    首页 = 参数[1]
                    back_home（信息，服务器，首页)
            其他：
                服务器。告诉（信息。播放器，“格式错误，输入！！首页 帮助来查看帮助信息”)
        埃利夫信息。内容。开头为（'！！设置主页“）：
            参数 = 信息。内容。分裂(' ')
            如果 len（args） == 1：
                主页 = “家”
                设置首页（信息，服务器，首页)
            Elif len（args） == 2：
                首页 = 参数[1]
                设置首页（信息，服务器，首页)
            其他：
                服务器。告诉（信息。播放器，“格式错误，输入！！首页 帮助来查看帮助信息”)
        埃利夫信息。内容。开头为（“！！德尔霍姆“）：
            参数 = 信息。内容。分裂(' ')
            如果 len（args） == 1：
                德尔霍姆='家'
                del_home（信息，服务器，德尔霍姆)
            Elif len（args） == 2：
                Delhome = args[1]
                del_home（信息，服务器，德尔霍姆)
            其他：
                服务器。告诉（信息。播放器，“格式错误，输入！！首页 帮助来查看帮助信息”)


#回家
定义back_home（信息，服务器，首页）：
    如果信息。家庭球员  ：
        错误 = 真
        对于我在  范围内（镜头（家庭[信息.播放器]））：
            如果在家里[信息。玩家][i]：
                服务器。告诉（信息。player， “§b将在3秒后传送回家”)
                暗光=家庭[信息。球员][i][主场][0]
                x = 家庭[信息。球员][i][主场][1]
                y = 家庭[信息.球员][i][主场][2]
                z = 家庭[信息.球员][i][首页][3]
                时间。睡眠（3)
                服务器。execute（'execute in {} run tp {} {} {} {}'.格式（tp_tran[暗]，信息。播放器， x， y， z))
                错误 = 假
        如果错误：
            服务器。告诉（信息。player，（“§b没有名为”，“''+home+'”'，“§b的家”))
    其他：
        服务器。告诉（信息。player，“§b请先建立家”)

#创建家
def sethome（info，server，home）：
    PlayerInfoAPI = server。get_plugin_instance（'PlayerInfoAPI')
    pos = PlayerInfoAPI。getPlayerInfo（server， info.播放器，路径='Pos')
    x = int（pos[0])
    y = int（pos[1])
    z = int（pos[2])
    dim = 玩家信息API。getPlayerInfo（server， info.播放器，路径='维度')
    如果信息。家庭球员  ：
        错误 = 真
        对于我在  范围内（镜头（家庭[信息.播放器]））：
            如果在家里[信息。玩家][i]：
                服务器。告诉（信息。player，“你已经有一个名为”+'“'+home+''+”的家了，请使用！！delhome删除后再创建”)
                错误 = 假
            打印（家庭[信息.玩家][i])
        如果错误：
            家[信息.玩家]。append（{home：[dim，x，y，z]})
            保存Json()
            服务器。告诉（信息。player，“§b已成功设定家”)
    其他：
        家[信息.播放器] = [{主页：[dim，x，y，z]}]
        保存Json()
        服务器。告诉（信息。player，“§b已成功设定家”)

#删除家
def del_home（info，server，delhome）：
    如果信息。家庭球员  ：
        错误 = 真
        对于我在  范围内（镜头（家庭[信息.播放器]））：
            如果德尔霍姆  在家里[信息。玩家][i]：
                德尔之家[信息.玩家][i]
                错误 = 假
                保存Json()
                服务器。告诉（信息。player，（“§b已成功删除名为”+'“'+delhome+'+”的家”))
                破
        如果错误：
            服务器。告诉（信息。player，“没有可删除的家，请先建立”)
    其他：
        服务器。告诉（信息。player，“没有可删除的家，请先建立”)


def on_load（服务器，旧）：
    全球家园
    服务器。add_help_message（'！！家庭帮助'， '家庭插件帮助')
    尝试：
        打开（json_filename）作为f：
            主页 = JSON。load（f， encoding='utf8')
    除了：
        保存Json()

#打印Home列表
def print_home（info，server）：
    服务器。告诉（信息。播放器，“§b主页列表”)
    如果信息。家庭球员  ：
        对于我在  范围内（镜头（家庭[信息.播放器]））：
            对于键，家庭中的值[信息。玩家][i].项目（）：
                暗淡 = 值[0]
                x = 值[1]
                y = 值[2]
                z = 值[3]
                如果 len（值） == 4：
                    服务器。告诉（信息。player，“名称：{} 坐标： §r{} §e{}， {}， {}”.格式（键， dim_tran[暗]， x， y， z))
    其他：
        服务器。告诉（信息。player，“没有已创建的家，请先建立”)

#保存json
def saveJson（）：
    将 open（json_filename， 'w'） 作为 f：
        杰森。dump（homes， f， indent=4)
