
---
title: 'Worker file manager 4.9.0 发布，开源文件管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=475'
author: 开源中国
comments: false
date: Mon, 30 Aug 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=475'
---

<div>   
<div class="content">
                                                                                            <p>Worker 是 UN*X 上的 X Window System 的一个双窗格文件管理器。目录和文件显示在两个独立的面板中，支持许多高级文件操作功能。它的主要重点是通过全键盘控制使文件管理变得简单，同时通过使用访问目录的历史记录、实时过滤和使用键盘访问命令来协助寻找文件和目录。</p> 
<p>Worker file manager 4.9.0 发布，更新内容如下：</p> 
<ul> 
 <li>新功能： 
  <ul> 
   <li>新注册的命令： 
    <ul> 
     <li>"show_entry" 进入给定名称的目录并突出显示基本名称</li> 
     <li>"vdir_add_entry" 在现有的虚拟目录中添加一个完整的路径名称，或者用该条目创建一个新的虚拟目录</li> 
     <li>"vdir_from_script_stack" 用一个选定的 ScriptOp 栈的所有元素创建一个新的虚拟目录</li> 
    </ul> </li> 
   <li>带有参数的注册命令现在也可以在 ScriptOp 和命令菜单中选择。在 ScriptOp 中，参数可以直接给出或通过动态标志替换。在命令菜单中，会出现一个询问参数的对话框，参数也可以直接输入或通过标志替换输入</li> 
   <li>chmod 命令现在可以被配置为直接应用一组给定的权限而不需要询问</li> 
  </ul> </li> 
 <li>改进： 
  <ul> 
   <li>根据 $HOME/.config/worker 中的 freedesktop 规范支持配置目录，而不是 $HOME/.worker。如果后一个目录存在的话，它仍然优先于前一个目录，所以不需要做任何改变，它只适用于新的安装。</li> 
  </ul> </li> 
 <li>修复： 
  <ul> 
   <li>修正了临时文件的问题： 
    <ul> 
     <li>如果 /tmp（或 $TMPDIR）被挂载为 noexec，则终端中的命令执行不起作用。必须改变要使用的终端的配置值以使其工作。默认值也会相应改变</li> 
     <li>如果 $TMPDIR 包含空格或其他特殊字符，命令的执行没有正常工作。由于缺少引号，作为 TMPDIR 字符串一部分的文件可能被无意中覆盖</li> 
    </ul> </li> 
   <li>修正了波兰语翻译中的 bug，该 bug 会在保存时将语言改回英语</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.boomerangsworld.de%2Fcms%2Fworker%2Fchanges.html%23org3ff016c" target="_blank">http://www.boomerangsworld.de/cms/worker/changes.html#org3ff016c</a></p>
                                        </div>
                                      
</div>
            