
---
title: 'Linux-vim编辑器'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11344802-9f09374d9757dd47.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11344802-9f09374d9757dd47.png'
---

<div>   
<h2>一. vi 编辑器简介</h2>
<p>vim 是一个全屏幕纯文本编辑器，是 vi 编辑器的增强版，我们主要讲解的是 vim 编辑器。可以利用别名让输入 vi 命令的时候，实际上执行 vim 编辑器，</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1250" data-height="142"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-9f09374d9757dd47.png" data-original-width="1250" data-original-height="142" data-original-format="image/png" data-original-filesize="16295" src="https://upload-images.jianshu.io/upload_images/11344802-9f09374d9757dd47.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image-20200513090913429.png</div>
</div>
<p>这样定义的别名是临时生效，如果需要永久生效，请放入环境变量配置文件（~/.bashrc）</p>
<h2>二. vim 基本使用</h2>
<h3>1. vim的工作模式</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1623" data-height="807"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-96ee4046e333980d.png" data-original-width="1623" data-original-height="807" data-original-format="image/png" data-original-filesize="143711" src="https://upload-images.jianshu.io/upload_images/11344802-96ee4046e333980d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p><strong>命令模式</strong>：是主要使用快捷键的模式，是我们后面学习的重点。命令模式想要进入输入模式，可以使用以下的方式</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1460" data-height="1043"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-46ac9e9c80952f4a.png" data-original-width="1460" data-original-height="1043" data-original-format="image/png" data-original-filesize="84130" src="https://upload-images.jianshu.io/upload_images/11344802-46ac9e9c80952f4a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>输入模式：主要用于文本编辑，和记事本类似，输入数据就好。</p>
<p>末行模式（编辑模式）：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2235" data-height="501"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-270a2926c03ca25d.png" data-original-width="2235" data-original-height="501" data-original-format="image/png" data-original-filesize="126160" src="https://upload-images.jianshu.io/upload_images/11344802-270a2926c03ca25d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">编辑模式</div>
</div>
<h3>2. 命令模式操作</h3>
<h4>2.1移动光标</h4>
<p>1）上下左右移动光标</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1022" data-height="141"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-643035dd806b8930.png" data-original-width="1022" data-original-height="141" data-original-format="image/png" data-original-filesize="21657" src="https://upload-images.jianshu.io/upload_images/11344802-643035dd806b8930.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">上下左右移动光标</div>
</div>
<p>2）把光标移动到文件头或尾</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1113" data-height="142"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-3c7f35acd5db9780.png" data-original-width="1113" data-original-height="142" data-original-format="image/png" data-original-filesize="23410" src="https://upload-images.jianshu.io/upload_images/11344802-3c7f35acd5db9780.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">把光标移动到文件头或尾</div>
</div>
<p>3）移动到行首或行尾</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1075" data-height="156"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-3839cf9994a374ef.png" data-original-width="1075" data-original-height="156" data-original-format="image/png" data-original-filesize="17952" src="https://upload-images.jianshu.io/upload_images/11344802-3839cf9994a374ef.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">移动到行首或行尾</div>
</div>
<p>4）移动到指定行</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="752" data-height="73"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-c55b570e03542d90.png" data-original-width="752" data-original-height="73" data-original-format="image/png" data-original-filesize="8794" src="https://upload-images.jianshu.io/upload_images/11344802-c55b570e03542d90.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">移动到指定行</div>
</div>
<p>这里 n 是数字，准备移动到第几行，就用哪个数字</p>
<h4>2.2 删除或剪切</h4>
<p>1）删除字母</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="856" data-height="147"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-f2ab771faa87687a.png" data-original-width="856" data-original-height="147" data-original-format="image/png" data-original-filesize="16851" src="https://upload-images.jianshu.io/upload_images/11344802-f2ab771faa87687a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">删除字母</div>
</div>
<p>n 是数字，如果打算从光标位置删除连续的 10 个字母，可以使用“10x”即可。删除字母并不符合使用习惯，我们更习惯在编辑模式中，用“Backspace”键删除字母。</p>
<p>2）删除整行或剪切</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="930" data-height="221"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-cbfd60842c7438d6.png" data-original-width="930" data-original-height="221" data-original-format="image/png" data-original-filesize="27057" src="https://upload-images.jianshu.io/upload_images/11344802-cbfd60842c7438d6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>删除整行或多行，这是比较常用的删除方法。这里的 dd 快捷键既是删除，也是剪切。删除内容放入了剪切板，如果不粘贴就是删除，如果粘贴就是剪切。粘贴方法</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1061" data-height="149"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-24bca603bb56aa0f.png" data-original-width="1061" data-original-height="149" data-original-format="image/png" data-original-filesize="19421" src="https://upload-images.jianshu.io/upload_images/11344802-24bca603bb56aa0f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>3）从光标所在行删除到文件尾</p>
<p>是否可以删除整篇文档，vim 没有删除整篇文档的快捷键，但是可以这样：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1180" data-height="73"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-410c67cd47499548.png" data-original-width="1180" data-original-height="73" data-original-format="image/png" data-original-filesize="15166" src="https://upload-images.jianshu.io/upload_images/11344802-410c67cd47499548.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>“d”是删除行，“G”是文件尾，连起来就是从光标所在行删除到文件尾。如果把光标放在文件首，那么“dG”就变成了删除整篇文档了。</p>
<h4>2.3 复制</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="712" data-height="139"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-9123f3307293fae5.png" data-original-width="712" data-original-height="139" data-original-format="image/png" data-original-filesize="12842" src="https://upload-images.jianshu.io/upload_images/11344802-9123f3307293fae5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>复制之后的粘贴，依然可以使用 p 键或 P（大）键</p>
<h4>2.4 撤销</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="955" data-height="147"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-da5278029ddd324e.png" data-original-width="955" data-original-height="147" data-original-format="image/png" data-original-filesize="13424" src="https://upload-images.jianshu.io/upload_images/11344802-da5278029ddd324e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">撤销</div>
</div>
<p>“u”键能一直撤销到文件打开时的状态，类似 Windows 下“ctrl+z”键的作用。</p>
<p>“ctrl+r”能一直反撤销到最后一次操作状态，类似 Windows 下“ctrl+y”键的作用。</p>
<h4>2.5 替换</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1198" data-height="147"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-7dec8ac233228c77.png" data-original-width="1198" data-original-height="147" data-original-format="image/png" data-original-filesize="32361" src="https://upload-images.jianshu.io/upload_images/11344802-7dec8ac233228c77.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">替换</div>
</div>
<p>“r”键替换单一字符，不用进入输入模式，实际使用时，比进入输入模式删除后再修改，要方便。</p>
<h4>2.6 vim配置文件</h4>
<p>这次末行模式参数设置, 多数需要在vim中才能生效</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2874" data-height="821"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-3548d75415b8844c.png" data-original-width="2874" data-original-height="821" data-original-format="image/png" data-original-filesize="272883" src="https://upload-images.jianshu.io/upload_images/11344802-3548d75415b8844c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">vim配置文件(一)</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2869" data-height="794"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b7c7a393d62fd91e.png" data-original-width="2869" data-original-height="794" data-original-format="image/png" data-original-filesize="248071" src="https://upload-images.jianshu.io/upload_images/11344802-b7c7a393d62fd91e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">vim配置文件(二)</div>
</div>
<p>vim支持更多的设置参数,可以通过“: set all”进行查看</p>
<p>​   大家会发现,这些设置参数都只是临时生效,一旦关闭文件再打开,又需要重新输入。如果想要永久生效,需要手工建立vim的配置文件“~/. vimrc”,把你需要的参数写入配置文件就永久生效了。</p>
<p>​   补充: Windows下回车符在 Linux中是用“M$”符号显示,而不是“$”符。这样会导致 Windows下编辑的程序脚本,无法在 Linux中执行。这时可以通过命令“dos2unix”,把 Windows格式转为 Linux格式,当然反过来“unix2dos”命令就是把 Linux格式转为 Windows格式。这两个命令默认没有安装,需要手安オ能使用</p>
<h4>2.7 查找</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1421" data-height="346"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b3ab95429c6bc4d5.png" data-original-width="1421" data-original-height="346" data-original-format="image/png" data-original-filesize="47685" src="https://upload-images.jianshu.io/upload_images/11344802-b3ab95429c6bc4d5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h4>2.8 替换</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1588" data-height="191"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-5210013bdf7e0625.png" data-original-width="1588" data-original-height="191" data-original-format="image/png" data-original-filesize="50198" src="https://upload-images.jianshu.io/upload_images/11344802-5210013bdf7e0625.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>shell 中“#”开头是注释,批量替换</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1377" data-height="182"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-d294f7d059765daf.png" data-original-width="1377" data-original-height="182" data-original-format="image/png" data-original-filesize="32608" src="https://upload-images.jianshu.io/upload_images/11344802-d294f7d059765daf.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">批量替换注释</div>
</div>
<p>而在 C 语言，PHP 语言等大多数语言中，是使用“//”开头作为注释的，我们当然可以用 vim 来写这些程序语言脚本，那么批量加入“//”注释吧：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1612" data-height="186"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-bea22fd8c2c3c7eb.png" data-original-width="1612" data-original-height="186" data-original-format="image/png" data-original-filesize="37872" src="https://upload-images.jianshu.io/upload_images/11344802-bea22fd8c2c3c7eb.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h2>三. vim 使用技巧</h2>
<h3>1. 在 vim 中导入其他文件内容或命令结果</h3>
<p>1.1 导入其他文件内容</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1444" data-height="89"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b070cb6f726c5dbc.png" data-original-width="1444" data-original-height="89" data-original-format="image/png" data-original-filesize="23581" src="https://upload-images.jianshu.io/upload_images/11344802-b070cb6f726c5dbc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>可以把其他文件的内容导入到光标所在位置</p>
<p>1.2 在 vim 中执行系统命令</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1551" data-height="90"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b2277defc910e230.png" data-original-width="1551" data-original-height="90" data-original-format="image/png" data-original-filesize="21593" src="https://upload-images.jianshu.io/upload_images/11344802-b2277defc910e230.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>这里只是在 vim 中执行系统命令，但并不把系统命令的结果写入到文件中。主要用于在文件编辑中，查看系统信息，如时间。</p>
<p>1.3 导入命令结果</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2407" data-height="90"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-cca92a3046e1488b.png" data-original-width="2407" data-original-height="90" data-original-format="image/png" data-original-filesize="38453" src="https://upload-images.jianshu.io/upload_images/11344802-cca92a3046e1488b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>在 vim 中执行系统命令，并把命令结果导入光标所在行。</p>
<h3>2. 设定快捷键</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2211" data-height="364"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-f7af9755187193e7.png" data-original-width="2211" data-original-height="364" data-original-format="image/png" data-original-filesize="130504" src="https://upload-images.jianshu.io/upload_images/11344802-f7af9755187193e7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>注意：^P 快捷键不能手工输入，需要执行 ctrl+V+P 来定义，或 ctrl+V ，然后 ctrl+P。^B 快捷键也是一样</p>
<h3>3. 字符替换</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2865" data-height="486"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-86c45845afb2c160.png" data-original-width="2865" data-original-height="486" data-original-format="image/png" data-original-filesize="212235" src="https://upload-images.jianshu.io/upload_images/11344802-86c45845afb2c160.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h3>4. 多文件打开</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2855" data-height="861"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b8e55335c4379640.png" data-original-width="2855" data-original-height="861" data-original-format="image/png" data-original-filesize="301825" src="https://upload-images.jianshu.io/upload_images/11344802-b8e55335c4379640.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
  
</div>
            