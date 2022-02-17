
---
title: 'fileboy v1.16 发布，文件变更监听通知工具，开发利器！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1514'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 11:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1514'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">fileboy，文件变更监听通知工具，支持多平台（<span style="background-color:#ffffff; color:#333333">Windows/Linux/MacOS</span>），使用 Go 编写。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">适用于 Hot Reload （典型的如开发go项目，无需每次手动执行 go build；又比如前端 node 打包） 或者 系统监控等任何需求感知文件变更事件的场景。  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>v1.16 更新日志：</strong></p> 
<ul> 
 <li>增加 -filegirl 参数，允许加载指定路径的配置</li> 
 <li>增加 pid 文件处理</li> 
 <li>增加 信息处理</li> 
 <li>优化 net client</li> 
 <li>优化 文件扫描性能</li> 
 <li>优化 一些细节</li> 
</ul> 
<p><strong>下载地址：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github:  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdengsgo%2Ffileboy%2Freleases%2Ftag%2Fv1.16" target="_blank">Windows  |  Linux  |   Mac</a>  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee:  <a href="https://gitee.com/dengsgo/fileboy/releases/v1.16">Windows  |  Linux  |  Mac</a>  </p> 
<p><strong>特性：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>极简的用法和配置</li> 
 <li>支持多平台，Windows/Linux/MacOS</li> 
 <li>支持自定义文件监听范围，监听指定文件夹/不监听指定文件夹/指定后缀文件</li> 
 <li>支持自定义监控事件（write/rename/remove/create/chmod）</li> 
 <li>支持设置多条命令</li> 
 <li>命令支持变量占位符</li> 
 <li>支持冗余任务丢弃，自定义冗余任务范围</li> 
 <li>支持 http 通知</li> 
</ul> 
<p><strong>快速使用：</strong></p> 
<pre><code class="language-bash"># bash terminal
cd /path/your/project
# init the config file filegirl.yaml
fileboy init
# edit the file filegirl.yaml to fit your project needs
vim filegirl.yaml
#run it, enjoy!
fileboy</code></pre> 
<p><strong>配置文件 filegirl.yaml示例说明：</strong></p> 
<pre><code>####################
## 配置文件说明
## 运行 fileboy 所在的路径为工作目录;
## 使用 -filegirl 命令参数可以加载指定路径的 filegirl 配置（不限定工作目录），如 "fileboy -filegirl /user/f/go.yml" 或者 "fileboy -filegirl ../../f/go.yml";
####################
# 主配置
core:
    # 配置版本号
    version: 1
# 监控配置
monitor:
    # 要监听的目录。必须是工作目录下的路径
    # test1       监听当前目录下 test1 目录
    # test1/test2 监听当前目录下 test1/test2 目录
    # test1,*     监听当前目录下 test1 目录及其所有子目录（递归）
    # .,*         监听当前目录及其所有子目录（递归）
    includeDirs:
        - .,*
    # 不监听的目录。必须是工作目录下的路径
    # .idea   忽略.idea目录及其所有子目录的监听
    exceptDirs:
        - .idea
        - .git
        - .vscode
        - node_modules
        - vendor
    # 监听文件的格式，此类文件更改会执行 command 中的命令
    # .go   后缀为 .go 的文件更改，会执行 command 中的命令
    # .*    所有的文件更改都会执行 command 中的命令
    types:
        - .go
    # 监听的事件类型，发生此类事件才执行 command 中的命令
    # 没有该配置默认监听所有事件
    # write   写入文件事件
    # rename  重命名文件事件
    # remove  移除文件事件
    # create  创建文件事件
    # chmod   更新文件权限事件(类unix)
    events:
        - write
        - rename
        - remove
        - create
        - chmod
# 命令
command:
    # 监听的文件有更改会执行的命令
    # 可以有多条命令，会依次执行
    # 如有多条命令，每条命令都会等待上一条命令执行完毕后才会执行
    # 如遇交互式命令，允许外部获取输入
    # 支持变量占位符,运行命令时会替换成实际值：
    #    &#123;&#123;file&#125;&#125;    文件名(如 a.txt 、test/test2/a.go)
    #    &#123;&#123;ext&#125;&#125;     文件后缀(如 .go)
    #    &#123;&#123;event&#125;&#125;   事件(上面的events, 如 write)
    #    &#123;&#123;changed&#125;&#125; 文件更新的本地时间戳(纳秒,如 1537326690523046400)
    # 变量占位符使用示例：cp &#123;&#123;file&#125;&#125; /root/sync -rf  、 myCommand --&#123;&#123;ext&#125;&#125; &#123;&#123;changed&#125;&#125;
    exec:
        - go version
        - go env
    # 文件变更后命令在xx毫秒后才会执行，单位为毫秒
    # 一个变更事件(A)如果在定义的延迟时间(t)内, 又有新的文件变更事件(B), 那么A会取消执行。
    # B及以后的事件均依次类推，直到事件Z在t内没有新事件产生，Z 会执行
    # 合理设置延迟时间，将有效减少冗余和重复任务的执行
    # 如果不需要该特性，设置为 0
    delayMillSecond: 2000
# 通知器
notifier:
    # 文件更改会向该 url 发送请求（POST 一段 json 文本数据）
    # 触发请求的时机和执行 command 命令是一致的
    # 请求超时 15 秒
    # POST 格式:
    #    Content-Type: application/json;charset=UTF-8
    #    User-Agent: FileBoy Net Notifier v1.16
    #    Body: &#123;"project_folder":"/project/path","file":"main.go","changed":1576567861913824940,"ext":".go","event":"write"&#125;
    # 例: http://example.com/notifier/fileboy-listener
    # 不启用通知，请留空 ""
    callUrl: ""
# 特殊指令
instruction:
    # 可以通过特殊的指令选项来控制 command 的行为，指令可以有多个
    # 指令选项解释：
    #   exec-when-start    fileboy启动就绪后，自动执行一次 'exec' 定义的命令
    #   should-finish      触发执行 'exec' 时(C)，如果上一次的命令(L)未退出（还在执行），会等待 L 退出（而不是强制 kill ），直到 L 有明确 exit code 才会开始执行本次命令。
    #                      在等待 L 退出时，又有新事件触发了命令执行(N)，则 C 执行取消，只会保留最后一次的 N 执行
    #   ignore-stdout      执行 'exec' 产生的 stdout 会被丢弃
    #   ignore-warn        fileboy 自身的 warn 信息会被丢弃
    #   ignore-info        fileboy 自身的 info 信息会被丢弃
    #   ignore-exec-error  执行 'exec' 出错仍继续执行下面的命令而不退出 
    #- should-finish
    #- exec-when-start
    - ignore-warn</code></pre> 
<p>如果使用中有 BUG 或建议，请您提 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdengsgo%2Ffileboy%2Fissues" target="_blank">Issue</a> 反馈。</p>
                                        </div>
                                      
</div>
            