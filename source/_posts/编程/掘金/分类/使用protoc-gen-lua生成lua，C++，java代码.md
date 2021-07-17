
---
title: '使用protoc-gen-lua生成lua，C++，java代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefdf3bdbee34d11a37ba68f626086c9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 06:36:34 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefdf3bdbee34d11a37ba68f626086c9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Protobuf 官方并没有 Lua版本，然后网易的程序猿开发出了 protoc-gen-lua ，可以让我们将 Proto 文件转成 lua 脚本在 Lua中使用，由于最后一直没人维护，貌似只能用proto2版本。</p>
<p>1、首先我们需要下载相关的资源</p>
<p>链接：链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1Khb-V7iFxCiFEJabB2s5hg" target="_blank" rel="nofollow noopener noreferrer" title="https://pan.baidu.com/s/1Khb-V7iFxCiFEJabB2s5hg" ref="nofollow noopener noreferrer">pan.baidu.com/s/1Khb-V7iF…</a> 提取码：6f0g</p>
<p>2、我们需要安装Python2.7</p>
<p>把安装目录添加到环境变量中，然后打开命令行 控制台，输入命令</p>
<p>python
出现下图，表示安装成功</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefdf3bdbee34d11a37ba68f626086c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、下载并编译 Luajit 2.0.4</p>
<p>下载后解压，找到 LuaJIT-2.0.4/src  目录，其中有一个批处理文件 msvcbuild.bat ，这是在 Windows系统的编译工具。在开始菜单 - 所有应用中的 Visual Studio 201x 中找到 Visual Studio Tools，打开 VS201x 开发人员命令提示，切换到 LuaJIT-2.0.4/src 目录，执行命令</p>
<p>msvcbuild.bat
到 LuaJIT-2.0.4\src 目录中寻找  lua51.dll  lua51.lib  luajit.exe 这三个文件是否存在，如果上面编译成功，那这三个文件是一定有的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4850be03f44c49cfbf13b9897976a85a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4、下载并编译 protobuf-2.4.1  (那些编译报错的地方我已经修复了，工程里已经生成了protoc.exe)</p>
<p>5、 到 protobuf-2.4.1\python 文件夹中执行命令</p>
<p>python setup.py install</p>
<p>​
6、组合文件</p>
<p>把这两个文件拷贝出来，并且把之前生成编译出来的一些文件拷贝过来(lua.exe 其实改了名字的,编译生成的是luajit.exe)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be358cb54124927975cf95777adb5a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>把protobuf-gen-lua的这两个文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c277a5c353d469d85c63dd8261f2bdd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>拷贝到这里面</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f45129a092154f7799c4d3220038aa3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>7.使用,这是我自己弄一个测试工具，上面三次对应生成C++，java，lua代码，protobuf文件夹才是之前生成那些文件存放地方</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80a1754871a341c3b376eb068bbc4a01~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d3ad6457bdd4fc6a12d6821e46ff2b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用的时候，运行这个proto2c++_lua.bat文件就会把这个目录下的所有.proto文件生成到上面三个对应语言的文件夹中，具体的逻辑在CreateCode里</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ea19cbd292469793f91893e22bea64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            