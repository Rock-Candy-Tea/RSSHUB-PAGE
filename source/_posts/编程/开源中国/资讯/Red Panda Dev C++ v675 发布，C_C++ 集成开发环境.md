
---
title: 'Red Panda Dev C++ v6.7.5 发布，C_C++ 集成开发环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-001da7e98b7188677280ada78b7886dbf37.png'
author: 开源中国
comments: false
date: Sat, 21 Aug 2021 00:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-001da7e98b7188677280ada78b7886dbf37.png'
---

<div>   
<div class="content">
                                                                                            <p>Red Panda Dev C++ v6.7.5 已经发布，小熊猫Dev-C++是一款小巧但功能强大的 C/C++ 编辑器，基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceforge.net%2Fp%2Forwelldevcpp%2F" target="_blank">Dev-C++</a>。</p> 
<p>VERSION 6.7.5 AUG 2021</p> 
<ul> 
 <li>改变：发行版改为使用msys2 mingw-w64 X86_64版64位GCC 10.3版本编译器（依然保留带32位GCC 9.2的 版本，以提供windows xp兼容）。因为TDM-GCC-64所带的gdb程序无法正确调试路径中带中文字符的程序。</li> 
 <li>功能增强：调试时，CPU窗口（可以通过“运行”菜单打开）以混合模式显示当前函数的反汇编结果。</li> 
 <li>修正：侧边栏代码浏览面板的“显示继承成员”按钮不起作用</li> 
 <li>修正：当字符串缺少结束双引号时，代码解析可能会出错。</li> 
 <li>功能增强：以只读模式打开系统头文件（以防误编辑）</li> 
 <li>改变：在有程序运行时，仍然可以运行/编译/调试程序（此时会提示是否关闭仍在运行中的程序以继续）</li> 
 <li>修正：代码分析器无法正确处理类多重继承</li> 
 <li>修正：新建项目调试出错</li> 
 <li>修正：海龟作图模板中存在拼写错误</li> 
 <li>修正：当调试器程序不存在时，启动调试会导致devcpp崩溃</li> 
 <li>修正：使用GLUT模板创建的项目无法编译</li> 
 <li>增加：GLFW+GLEW项目模板（用于学习现代OpenGL编程） VERSION 6.7.4 AUG 2021</li> 
 <li>改变：使用TDM-GCC 64位GCC 10.3版本编译器（依然保留32位GCC 9.2 版本，以提供windows xp兼容）</li> 
 <li>修正：使用相对路径保存项目缺省文件夹</li> 
 <li>修正：无法插入日期 VERSION 6.7.3 JUNE 2021</li> 
 <li>改变：在编译项目时自动生成的makefile文件中，使用del /q代替rm.exe</li> 
 <li>修正：不能正确显示GDB注解信息（需要在环境选项对话框中打开）</li> 
 <li>修正：’]’的符号自动补全选项不能正常工作</li> 
 <li>实验性提供对clang的支持（使用msys2提供的64位版本）</li> 
 <li>已知问题：clang所带的gdb不能正确支持路径中带非ASCII字符的问题（如果源文件所在路径包含中文字符，会无法设定断点）</li> 
 <li>已知问题：clang不支持文件编码参数（在中文windows下不要用UTF-8编码编辑和保存文件）</li> 
 <li>已知问题：代码分析器不能正确解析libc++库中的头文件，因此在编辑时无法正确显示代码补全提示（delphi版本不再处理该问题，待QT版本实现） VERSION 6.7.2 JUNE 2021</li> 
 <li>修正：调试时，不能显示鼠标指向的变量的内容</li> 
 <li>功能增加：使用汇编语言语法高亮显示.s和.asm后缀的文件。</li> 
 <li>改变：gcc 10.3中的gdb改用msys2提供的版本。（更稳定，且在调试时可以更方便的查看STL容器中的内容）。 VERSION 6.7.1 MAY 2021</li> 
 <li>修正：项目选项对话框中，库目录和包含目录页的标题错误</li> 
 <li>修正：在执行gcc -v检测编译器版本信息时，添加LANG=en环境变量，以避免其自动翻译输出信息，导致dev-cpp无法正确解析</li> 
 <li>修正：gcc 10.2中带的gdb.exe无法正确调试</li> 
 <li>更新：gcc 10升级为10.3 VERSION 6.7 MAY 2021 VERSION 6.7-BETA5 MAY 2021</li> 
 <li>修正：如果屏幕宽度小于补全提示框的宽度，不能正确显示提示内容</li> 
 <li>修正：在编译器选项对话框中通过指定文件夹来添加编译器设置时，新增的设置未能正确保存。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-001da7e98b7188677280ada78b7886dbf37.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-bad535dc3dd71aded1c941caffd3233667e.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-180482789a94f019e1bd5f7f1e134b73a35.png" referrerpolicy="no-referrer"></p> 
<p>详情查看：<a href="https://gitee.com/royqh1979/Dev-CPP/releases/v6.7.5">https://gitee.com/royqh1979/Dev-CPP/releases/v6.7.5</a></p>
                                        </div>
                                      
</div>
            