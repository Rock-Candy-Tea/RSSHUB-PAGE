
---
title: '合理使用WebStorm-环境配置篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e855ca735c94c72aabdbe57b3bbf110~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 08:07:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e855ca735c94c72aabdbe57b3bbf110~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>使用webstorm做为前端开发工具已经3年多时间了，抽空来记录下我常用的一些插件和配置，欢迎各位感兴趣的开发者阅读本文。</p>
<h2 data-id="heading-1">环境配置</h2>
<p>首先，我们打开<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jetbrains.com%2Fwebstorm%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jetbrains.com/webstorm/download/" ref="nofollow noopener noreferrer">webstorm官网</a>根据自己的系统下载对应的安装包。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e855ca735c94c72aabdbe57b3bbf110~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719225511397" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">安装软件</h3>
<p>打开我们下载好的安装包，按照下图所示步骤进行安装。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25873166e0b24c3ea5188b024dc4877f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719225838867" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>选择安装路径</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dc1398a5cfb4d13a16a0f41f7927679~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719225951563" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>选择要安装的版本以及默认文件关联</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83f5c41b4a5d4636a20994b1e6948204~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719230156845" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>开始安装</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1deca40eed0400397455b9c3e833a12~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719230229295" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装中...</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ad02a18059a4b16baa006298316131b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719230306253" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装完成，重启电脑</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd8080174fb14e0ab3a09364b723b450~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719230732445" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">启动软件</h3>
<p>安装完成后，双击桌面图标来启动它。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06736069465c4ef6b5e721490f6b0052~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719232504013" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>发送崩溃信息日志等到jet帮助他们改进产品，可以按照自己的需求选，此处选择发送。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53aed196bd1a4b3e8ad6ef21df136935~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719233201267" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>选择免费试用，填写自己的邮箱即可</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a5cb67b5d4427eaff16ac2a7ffd6a8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719233532472" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">配置软件</h3>
<p>在软件启动界面，打开你的项目。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/169446fe28b74432b6f59281acac900b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719234543701" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>打开项目中任意一个文件，这个界面看起来可能有点丑，后面我们会让他脱胎换骨</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336f2a38f1a34d8491159632c14e75f5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719234951634" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">修改字体与行高</h3>
<p>以此选择菜单栏的<code>File - Settings</code>打开软件的设置面板。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29171ed845bc4cd595e4b3601c92e812~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719235316208" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>按照下图所示修改字体、大小、行高、开启连字符</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db270a9ecfc4486487ebe5611ab2d6e8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210719235546600" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">常用插件</h2>
<p>接下来，我们安装几个插件，让webstorm脱胎换骨。</p>
<h3 data-id="heading-7">主题插件</h3>
<p>首先要安装的是主题插件<code>Material Theme UI</code>，打开软件的设置面板找到，<code>Plugins</code>，搜索这个插件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/132e9a621c3d43dc8c33b5ec2148bf15~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000136770" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装中...</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb215548359a4da1ac100dacfc076ee8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000226973" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装成功，重启webstorm</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9786ad9d9ce443fbaf435f90a95c11f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000309157" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">安装图标插件</h3>
<p>安装完主题插件后，界面稍微好看了那么一点，但是图标还是默认的，很是不搭配，我们继续在<code>Plugins</code>中搜索<code>Atom Material Icons</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b03d4f58c44749d2a38728cc014c15c6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000824116" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装中...</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf848d9d261240afb6ea5f4bd306ec88~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000845996" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装成功，应用更改，手动重启webstorm。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f67cea9517b345c9b90b67b823455aa9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720000941830" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">更换主题</h3>
<p>安装完主题插件和图标插件后，我们还需要在<code>Settings</code>面板中切换主题</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c01183e6182411ba8bb6acdafda9d95~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720001708274" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在打开的面板中，在<code>Theme</code>选项那里选择你喜欢的主题，此处选择<code>Atom One Dark (Material)</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3593eaf7da88410fb89d9ccea7888fd0~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720001959996" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在<code>Editor - Font</code>面板中修改主题字体</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6051d590125a4dd084d2a33f9c597753~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720002152088" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72cbeb6142874c20a8c9272b5656abbf~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720002314482" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>配置完成后的效果</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc898f3fc6a540cf8868226b5615e585~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720002437306" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">翻译插件</h3>
<p>英语不是很好的开发者，为变量起名时，遇到词穷的情况时，大多数情况会打开翻译网站翻译过后再粘贴过来，webstorm有一款名为<code>Translation</code>的插件，可以做到选中中文直接右键翻译并替换。</p>
<p>我们在插件商店中搜索安装即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/428884db9af346d2876a068406bcdfbd~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720002918264" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装完成后，在编辑器中输入中文，右键即可翻译，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2735fcebef5452ab093b9398ec1cbe4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720003320120" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5471daffb5bc49b8961c20d631e3c1c8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720003336242" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">git提交模版</h3>
<p>我们在使用git提交代码时，团队如果制定了提交规范，可能需要自己去写提交前缀，在webstorm中有一个名为<code>Git Commit Template</code>的插件，可以手动选择类型，自动帮我们补齐前缀。</p>
<p>在插件商店中搜索安装即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b122362a6148ad9eb8c9e2963974a9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720003808245" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们随便改点项目中的代码，然后选择菜单栏的<code>git - commit</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08df9db9caa44449b0d2aef777e64162~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720004508661" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>默认是在项目左侧显示，我们把它改为弹窗形式显示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac1f6e6d58d42f2ad5cdd20eac23264~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720004631719" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击模版图标，即可打开提交选项</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cacdcbf12e7a49fda40025ab950714b7~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720004809668" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>按照自己更改的内容，按需选择填写即可</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddb517d1dbab4cb0936939b6478bc1f1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720004935379" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>填写完成，将会回到提交页面，自动填写我们刚才所选择的选项</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4b2ac22e334249bcf8663285af07bd~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720005051274" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">Git提交记录</h3>
<p>维护项目时，发现bug，我们想快速知道这行代码是谁提交的，大部分开发者可能要去通过<code>git log</code>来查找。</p>
<p>在webstorm中，有一个名为<code>GitToolBox</code>的插件，当我们鼠标选择某一行代码时，就能显示出这行代码的提交人和提交时间。</p>
<p>在插件商店搜索安装</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2266854e00984892a33b953f234a880c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720005537135" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装完成，重启编辑器</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e400b943489248409743a7f46b5ddda2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720005618211" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>鼠标选中代码，这一行的末尾就会显示提交人、提交时间等信息</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89fd12115825401aa481b39ba408d24c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720005737054" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">AI代码联想工具</h3>
<p>webstorm中还有一款名为<code>Codota</code>的插件，他可以在你写代码时，自动联想出你想输入的内容。</p>
<p>在插件商店中搜索安装即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5aa37f7c784e5f89e24ea3f51f2f9c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720010111488" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装完成，重启编辑器，打开<code>setting-Codota</code>面板，将其启用</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e27293fc11d43a581a067b1823093e5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720010636730" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>随便写点代码即可看到效果</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e589b4c8b40c4a59801be05cb96b8501~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720010451528" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">文件忽略</h3>
<p>我们在项目中不想让把某个文件上传到git，通常情况下我们需要自己往<code>.gitignore</code>文件中去添加要忽略的文件，在webstorm中有一款名为<code>.ignore</code>的插件，可以通过右键不想上传的文件即可实现将其添加到配置文件中。</p>
<p>在插件商店中搜索安装即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc9a11140246401cb8b171a7db317234~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720011017473" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>右键，添加到忽略文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22fb22f5ed5e4e91ad069efd446662f2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720011244740" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-15">最终效果</h2>
<p>完成上述配置后，webstorm已经算是脱胎换骨了，但是还是觉得编辑器周围显示的选项卡有点多，我选择把它隐藏起来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a2fceecfdbe4fe7881d3c35a3b29e22~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720012629644" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>最终界面如下所示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdd5c80fe0294895abdab9086f930d25~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210720012713110" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：四周的选项卡隐藏后，在mac系统上可以通过双击command键让其显示出来。</p>
<p>windows系统则需要设置快捷键让其显示出来，我们打开srttings面板在keymap中搜索<code>Tool Window Bars</code>然后设置快捷键。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a123ced179048ed93e4f10a492d3cc7~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721222227391" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846adb88e84642a2b60585a383accac3~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721222402431" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bd3aaa6a74a4653848bec741038fc59~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721222425419" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-16">其他配置</h2>
<p>此处再列举一些项目上的配置。</p>
<h3 data-id="heading-17">Eslint的配置</h3>
<p>有关Eslint的配置请移步我的另一篇文章：<a href="https://juejin.cn/post/6850418115995287566#heading-4" target="_blank" title="https://juejin.cn/post/6850418115995287566#heading-4">配置编辑器</a></p>
<h3 data-id="heading-18">构建项目索引</h3>
<p>当你在写代码时，发现vue的一些内置指令、elementUI的一些组件无代码提示时，就需要构建下项目索引了，操作方法如下：</p>
<ul>
<li>在<code>node_modules</code>文件夹上右键，在弹出的选项中选择<code>Mark Directory as -Not Excluded</code>即可</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92bf15a2108546bebbbc66eab5c568c6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721220710616" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">一些常用的快捷键</h3>
<ul>
<li>
<p>选中当前行代码：<code>command shift ⬅️/command shift ➡️</code></p>
</li>
<li>
<p>移动当前行代码：<code>command ⬆️/ commind ⬇️</code></p>
</li>
<li>
<p>提交代码到git本地：<code>command K</code></p>
</li>
<li>
<p>push代码到git远程仓库: <code>comnand shift K</code></p>
</li>
<li>
<p><code>shift</code> 按两次，随处搜索，搜索文件、功能、代码很方便</p>
</li>
<li>
<p>command + f  当前页搜索</p>
</li>
<li>
<p>command + shift + f  全局搜索字段</p>
</li>
<li>
<p>command + r 替换当前文档</p>
</li>
<li>
<p>command + shift + r 全局替换字段</p>
</li>
<li>
<p>command + option + l 格式化代码</p>
</li>
<li>
<p>shift + f6 使文件、标签、变量名重命名</p>
</li>
<li>
<p>f2, shift + f2 切换到上\下一个突出错误的位置</p>
</li>
<li>
<p>shift + 回车  无论在什么位置，自动跳到下一行</p>
</li>
<li>
<p>option + 回车 警告代码快速给出自动修正</p>
</li>
<li>
<p>command + 左键点击  跳到代码调用位置</p>
</li>
<li>
<p>command + delete 删除当前行</p>
</li>
<li>
<p>command + d 复制新增一行一样的代码</p>
</li>
<li>
<p>command + w  关闭当前文件选项卡</p>
</li>
<li>
<p>command + /    注释行代码</p>
</li>
<li>
<p>command + b   跳转到变量声明处</p>
</li>
<li>
<p>command + shift + c  复制文件的路径</p>
</li>
<li>
<p>command + shift + [ ]  选项卡快速切换，很有用</p>
</li>
<li>
<p>command + shift + +/-  展开/折叠 当前选中的代码块</p>
</li>
</ul>
<h3 data-id="heading-20">将某一块代码提炼成一个方法</h3>
<p>用鼠标选中一块代码，按下：<code>command+option+m</code>即可自动将这部分代码提炼成一个方法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a89900797a8c43209e8279a2dd27e1e6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721234032254" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">配置备份</h3>
<p>点击下图所示图标（编辑器底部），点击登录自己账号即可完成同步</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b58f8fa0ba91471aa16705a397613cb8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721232319259" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：如果你看不到这一栏，则需要在<code>view - status Bar</code>开启</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/020bce418d6647e98b3687d65696206d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721232611336" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-22">禁止掉不用的插件</h3>
<p>在<code>help</code>菜单下禁用，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85b49c93d9bc412897d4c9b5b6eef225~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721235131850" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再打开的面板中，选中你想禁用的插件点ok即可，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/207842d81bfc4a0d88b0ac7bd56bd2a2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210721235319352" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">申请许可证</h2>
<p>webstorm是付费的，官方有开放开源项目申请渠道，通过后可以免费使用1年，过期了可以接着申请续期，一般项目维护在 3 个月以上大概率可通过。</p>
<p>申请地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fcommunity%2Fopensource%2F%23support" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jetbrains.com/zh-cn/community/opensource/#support" ref="nofollow noopener noreferrer">开源项目许可证</a></p>
<h2 data-id="heading-24">写在最后</h2>
<p>至此，文章就分享完毕了。</p>
<p>我是<strong>神奇的程序员</strong>，一位前端开发工程师。</p>
<p>如果你对我感兴趣，请移步我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.kaisir.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.kaisir.cn/" ref="nofollow noopener noreferrer">个人网站</a>，进一步了解。</p>
<ul>
<li>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞和关注😊</li>
<li>本文首发于掘金，未经许可禁止转载💌</li>
</ul></div>  
</div>
            