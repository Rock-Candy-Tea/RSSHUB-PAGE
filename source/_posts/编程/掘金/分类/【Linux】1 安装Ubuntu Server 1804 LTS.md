
---
title: '【Linux】1. 安装Ubuntu Server 18.04 LTS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605c4167deb3403d91a6a684cb58ab0f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 02:57:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605c4167deb3403d91a6a684cb58ab0f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>虚拟机环境：VMware Workstation 15.5 Pro</p>
<p>Linux系统：Ubuntu-18.04.2-live-server-amd64</p>
<h3 data-id="heading-0">安装步骤</h3>
<ol>
<li>点击VMward主页的 <code>创建新的虚拟机</code> 按钮</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/605c4167deb3403d91a6a684cb58ab0f~tplv-k3u1fbpfcp-zoom-1.image" alt="图：创建虚拟机" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>弹窗 <code>新建虚拟机向导</code> 页面，该页面选择 <code>自定义</code> 选项，然后选择 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35fcbf88cfa245cca3aff50961ddab06~tplv-k3u1fbpfcp-zoom-1.image" alt="图：自定义" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>虚拟机硬件兼容性，选择最新的 <code>Workstation 15.X </code>，继续 <code>下一步</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b402a3eedaf442c285ea8cb5489ed3c2~tplv-k3u1fbpfcp-zoom-1.image" alt="图：选择兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>安装来源，选择 <code>稍后安装操作系统</code> 选项，继续 <code>下一步</code></p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba0b148a7b8c40168a7dd6e0d6f16516~tplv-k3u1fbpfcp-zoom-1.image" alt="图：稍后安装OS" loading="lazy" referrerpolicy="no-referrer">
5. 客户机操作系统选择 <code>Linux</code> ，版本选择 <code>Ubuntu 64位</code> ，继续 <code>下一步</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88cef1507f3410fbf888eee95fae9b4~tplv-k3u1fbpfcp-zoom-1.image" alt="图：OS类型" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>输入 <code>虚拟机名称</code>，选择 <code>安装位置</code> ，继续 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fb6fa63940d41c99aa631d1ea282778~tplv-k3u1fbpfcp-zoom-1.image" alt="图：命名虚拟机" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>根据实际情况选择 <code>处理器数量</code>和 <code>每个处理器的内核数量</code> 。一般选择1处理器2内核。继续 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82a2b8bef26145e6926e88ab7b3dc7c3~tplv-k3u1fbpfcp-zoom-1.image" alt="图：处理器配置" loading="lazy" referrerpolicy="no-referrer">
8. 根据实际需求选择虚拟机的内存，继续 <code>下一步</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec57ac3298d4fa7a366e2a437aa1191~tplv-k3u1fbpfcp-zoom-1.image" alt="图：内存配置" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="9">
<li>网络类型，选择 <code>使用网络地址转换NAT</code>，继续 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66f4cf2a79154adfaead2a6b25ebe797~tplv-k3u1fbpfcp-zoom-1.image" alt="图：网络配置" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="10">
<li>控制器和硬盘等，均选择默认选项即可，如下图所示。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ce3e2a4ec08406697cc2a79599944b6~tplv-k3u1fbpfcp-zoom-1.image" alt="图：IO控制" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b0913d3b346434085104c06311efaa1~tplv-k3u1fbpfcp-zoom-1.image" alt="图：磁盘类型" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e092b83bb6fb44d4a4c5f323b3bb97b6~tplv-k3u1fbpfcp-zoom-1.image" alt="图：选择磁盘" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="11">
<li>磁盘容量选择根据需求填写，指定磁盘文件选择默认即可，如下图所示。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/249357b64ce148cd8e00454f9d3d9686~tplv-k3u1fbpfcp-zoom-1.image" alt="图：磁盘容量" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b76a473a7a248f2bcc28a4531b5aea2~tplv-k3u1fbpfcp-zoom-1.image" alt="图：磁盘文件" loading="lazy" referrerpolicy="no-referrer">
12. 完成上述，点击 <code>完成</code> 按钮即可创建，如下图所示。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3631872f5dbc48ee97776f1b21176cdd~tplv-k3u1fbpfcp-zoom-1.image" alt="图：完成创建" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="13">
<li>点击虚拟机设备处的光驱，如下图</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/940ea208fbca4645ada70519f6594d71~tplv-k3u1fbpfcp-zoom-1.image" alt="图：进行安装OS" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="14">
<li>勾选 <code>使用ISO镜像文件</code> ，并指定Ubuntu的iso镜像文件，然后 <code>确定</code> 即可。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34050aec401041059f3ddda370d74fee~tplv-k3u1fbpfcp-zoom-1.image" alt="图：选择镜像" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11de8f6bfcf147a5bf6a5b0664e96b2f~tplv-k3u1fbpfcp-zoom-1.image" alt="图：完成选择" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="15">
<li>点击 <code>开启此虚拟机</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7845c04c1f740bb8868e45ba7508ca5~tplv-k3u1fbpfcp-zoom-1.image" alt="图：开启虚拟机" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="16">
<li>第①步：选择语言 <code>English</code> ，按 <code>回车</code> 选定</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7822c238737a4a8a8966387bfd531dcb~tplv-k3u1fbpfcp-zoom-1.image" alt="图：选择语言" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="17">
<li>第②步：键盘布局默认English即可，按 <code>回车</code> 确定</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9ca88426f154623913dc5ba68afb483~tplv-k3u1fbpfcp-zoom-1.image" alt="图：布局" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="18">
<li>第③步：选择第一项正常安装Ubuntu即可</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac9ecf5eafe4dc3807567d8fa839533~tplv-k3u1fbpfcp-zoom-1.image" alt="图：安装类型" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="19">
<li>第④步：显示的是虚拟机的网卡地址，默认即可，无需改动，点击确定</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8945fe63d114a4da93de982c111af18~tplv-k3u1fbpfcp-zoom-1.image" alt="图：网卡" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="20">
<li>第⑤步：代理地址默认为空即可，继续下一步</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e74b76661ad244b78e24621ffcaea50f~tplv-k3u1fbpfcp-zoom-1.image" alt="图：代理地址设置" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="21">
<li>第⑥步：按 <code>Tab</code> 键切换至 <code>镜像地址</code> 输入框，替换成阿里云的镜像地址，如下图所示，然后再确定</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed917b9acf9c4309a241478039b0ec43~tplv-k3u1fbpfcp-zoom-1.image" alt="图：镜像地址替换" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="22">
<li>第⑦步：选择第二项磁盘扩容技术</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/060e78bb41e145d08a11e9ff05f39790~tplv-k3u1fbpfcp-zoom-1.image" alt="图：磁盘扩容技术" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="23">
<li>这是第一块硬盘的名字sda，按回车继续即可</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2820d80c1dce4c18aab605de2b758e0c~tplv-k3u1fbpfcp-zoom-1.image" alt="图：硬盘命名" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="24">
<li>按键盘↑，切换到逻辑卷 <code>lv</code> 行，按 <code>回车</code> 唤出选项，选择 <code>Edit</code> ，然后修改数据为最大值，其他值保存默认，保存</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f463165fcbf642888ac09d4a2b284d82~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改数据为最大值：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0624099626184cd9a1ec36a93b00cb92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改后如下图所示，然后继续
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fe19cce5948447bb91358314c5cb86d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="25">
<li>弹窗选择 <code>继续</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81c0987ac8374de49427baeb72f3afc2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="26">
<li>输入<code>名字、密码</code>等数据，然后<code>继续</code>。虚拟机的密码一般用123456即可</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c5e9671107e4d0fb700f04f58549db0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="27">
<li>这里按 <code>空格</code> 键，开启SSH，然后 <code>上下键</code> 切换到 <code>Done</code> 按钮，继续</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c30cd9e9474563974693aa5151ad5d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="28">
<li>这个页面没有需要安装的，按 <code>Tab</code> 键，切换至 <code>Done</code> 按钮，确定</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc7c552f2764444a8624e2b9030bb09a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="29">
<li>系统正在安装……</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce555c07c1194e76b71c9a3dc4c3b9fe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="30">
<li>安装成功，选择 <code>重启</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9599b77e6a9f43bdb930d321580e955f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="31">
<li>如果重启时，弹出什么按Enter继续，根据提示操作即可。<strong>如果没有弹出，则忽略此步骤</strong>。</li>
<li>系统开机成功</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbd633b9692e43faae7f2f5dd56cde62~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="33">
<li>输入 <code>用户名</code> 和 <code>密码</code> ，登录成功</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e414c6990e6e4053a350540f8dec363a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="34">
<li>关机命令：<code>shutdown -h now</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52ee2257802a4ab3afd517794ad585e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上是在虚拟机中安装ubuntu的全部过程。</p>
<h3 data-id="heading-1">克隆虚拟机</h3>
<p>上述安装的虚拟机，一般不用，练习开发时，用到的是这个虚拟机的克隆。意思就是，克隆的虚拟机随便玩，玩坏了，就再克隆一个，减少重装的复杂过程。</p>
<ol>
<li><code>右键</code>上述安装的虚拟机，选择 <code>管理</code> ——》 <code>克隆</code>，如下图：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abdc0ed860e5439e8e3264a870adacca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>默认 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc106fe5ca7429c93bfdc0e96da803f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>选择 <code>第一项</code>，继续 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18ddde2df16455a8b8cccf6bf022f04~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li><code>创建链接克隆</code> 即可，然后选择 <code>下一步</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2d36bd522b241c7805a3e9502bef5a9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>输入克隆虚拟机的 <code>名字</code> 和 <code>安装位置</code> ，然后点击 <code>完成</code> 即可。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f92c2a0e8fd4e568f1692218c77c651~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>克隆完成， <code>关闭</code> 即可。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e021d97e194b4c52a31d829dfd175573~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li><code>开启</code> 克隆的虚拟机</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3de89eaaa464727be98be751e2ddf92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="8">
<li>输入 <code>用户名和密码</code> ，用户名和密码同安装Ubuntu时，设置的一致。成功进入，大功告成。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3001f38fa7478780aac3d2dd9c2ff6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上。</p></div>  
</div>
            