
---
title: 'Spark-Store 3.0.3-8 发布，Wine 应用商店'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4132'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 00:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4132'
---

<div>   
<div class="content">
                                                                                            <p>Spark-Store 3.0.3-8 已经发布，Wine 应用商店。</p> 
<p>此版本更新内容包括：</p> 
<p><strong>更新内容：</strong></p> 
<ul> 
 <li>不再与最新版本的spark-dstore-patch冲突</li> 
 <li>现在默认不会显示已集成dstore patch的信息了，仅在同时安装了patch后显示</li> 
 <li>安装时会同时加入新的密钥，旧的将会在不久后废除，所以请尽快更新到3.0.3-8+版本</li> 
 <li>这回记住修改关于界面的版本号了</li> 
</ul> 
<hr> 
<p>特性:spk</p> 
<p>见到spk://开头的链接，只要在浏览器里打开/复制到星火商店的搜索栏就可以直接跳转到星火商店的对应页面了</p> 
<h2>如果依赖报错先执行sudo apt update更新软件源，大部分需要依赖的应用会有补充依赖在星火的源里，只要更新源就能正常安装</h2> 
<p>推荐安装应用：</p> 
<div> 
 <pre><code>web-packer
网页打包工具：只需要网址和图标就能获得可以投稿的应用！
下载链接：https://gitee.com/deepin-community-store/web-packer/releases/
spk://store/tools/spark-web-packer

a2d
Appimage一键生成deb，只需要appimage包就可以投稿岂不美哉？
spk://store/development/appimage2deb

Uengine运行器
让自带的Uengine可以运行自定义apk！还可以打包成deb！
spk://store/tools/spark-uengine-runner

右键刷新
虽然没什么用，但是可以解压
spk://store/tools/sm-refresh

共享文件夹
右键直接打开一个共享工具，手机扫码即可局域网传输！
spk://store/tools/sendbylan

HMCL
著名我的世界启动器
spk://store/games/store.spark-app.hmcl

微信（wine）
显然是好文明
spk://store/chat/com.qq.weixin.spark

微信（Linux）
也是官方版，猜猜怎么得到的
spk://store/chat/wechat-linux-spark

钉钉（Linux）
官方公测包
spk://store/chat/com.alibabainc.dingtalk

PhotoGimp
长的很像PS的Gimp
spk://store/store/photogimp

蜘蛛纸牌
嗯，它完全是为了证明我们有个webapp运行环境，只是为了引导你在搜索栏搜索web。比如sans模拟器还有fairdyne，高德地图，OCR什么的。不知道把这个说出来了你会不会搜了。。。当然，你确实可以玩蜘蛛纸牌！
spk://store/games/spider-card
</code></pre> 
 <div>
   
 </div> 
</div> 
<p>星火商店Q&A:</p> 
<p>Q-2 我在使用UOS但我不想打开开发者模式 A-2 看看这个：<a href="https://gitee.com/deepin-community-store/spark-store-uos/releases" target="_blank">https://gitee.com/deepin-community-store/spark-store-uos/releases</a></p> 
<p>Q-1 去哪反馈？ A-1 应用详情页面有按钮</p> 
<p>Q0 在哪里投稿？ A0 右上角菜单--->投递应用</p> 
<p>Q1. 我不是deepin/UOS用户，可以使用星火应用商店吗？ A1: 可以，但是请先下载依赖补充包</p> 
<p>Q2. 下载的web应用不能启动怎么办？ A2：</p> 
<div> 
 <pre><code>如果你在使用ubuntu 20.04，推荐更新dtk到5.4版本，也可参考Debian11的解决方法
如果你是使用Debian 11的用户，理论上不会出问题，如果闪退，请卸载spark-webapp-runtime并下载swrt-lite包来修复
sudo apt remove spark-webapp-runtime -y && sudo apt install swrt-lite -y
</code></pre> 
 <div>
   
 </div> 
</div> 
<p>Q3. wine应用不能启动 A3. 带上你的发行版名称&版本去应用反馈/催更</p> 
<p>Q4. 星火商店会影响系统正常更新吗？ A4. 星火商店的源优先级被调的低于系统默认，不会影响</p> 
<p>Q5. 应用界面很灰，很亮，看不清怎么办 A5. dtk限制，暂时没什么办法，将就用吧</p> 
<p>Q6. 关于按钮打不开，一打开就闪退 A6.</p> 
<div> 
 <pre><code>如果你用的是ubuntu 20.04，请尝试更新dtk到5.4版本（仓库已经同步更新）
    如果你用的是Debian11:理论上不会了，如果不要点还是闪退，那就
</code></pre> 
 <div>
   
 </div> 
</div> 
<p>想到了再更</p> 
<p>详情查看：<a href="https://gitee.com/deepin-community-store/spark-store/releases/3.0.3-8">https://gitee.com/deepin-community-store/spark-store/releases/3.0.3-8</a></p>
                                        </div>
                                      
</div>
            