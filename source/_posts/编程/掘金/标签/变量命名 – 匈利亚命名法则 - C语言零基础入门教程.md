
---
title: '变量命名 – 匈利亚命名法则 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dce7d95a304e5aaedc13c89169f956~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 16:18:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dce7d95a304e5aaedc13c89169f956~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">变量命名 – 匈利亚命名法则 - C 语言零基础入门教程</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5dce7d95a304e5aaedc13c89169f956~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FZhaDeNianQu" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ZhaDeNianQu" ref="nofollow noopener noreferrer">猿说编程</a> 2021-07-31 08:14:43 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a68d0b94ba4f463dab8179a077e7a5dd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efaf52468e234bb191ce0e2c453473e1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"> 收藏</p>
<p>文章标签： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.csdn.net%2Ftags%2FMtjaMg3sOTYzMTEtYmxvZwO0O0OO0O0O.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.csdn.net/tags/MtjaMg3sOTYzMTEtYmxvZwO0O0OO0O0O.html" ref="nofollow noopener noreferrer">变量命名</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fso.csdn.net%2Fso%2Fsearch%2Fs.do%3Fq%3D%25E5%258C%2588%25E5%2588%25A9%25E4%25BA%259A%25E5%2591%25BD%25E5%2590%258D%25E6%25B3%2595%25E5%2588%2599%26t%3Dblog%26o%3Dvip%26s%3D%26l%3D%26f%3D%26viparticle%3D" target="_blank" rel="nofollow noopener noreferrer" title="https://so.csdn.net/so/search/s.do?q=%E5%8C%88%E5%88%A9%E4%BA%9A%E5%91%BD%E5%90%8D%E6%B3%95%E5%88%99&t=blog&o=vip&s=&l=&f=&viparticle=" ref="nofollow noopener noreferrer">匈利亚命名法则</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.csdn.net%2Ftags%2FMtTakgzsMjE0NTMtYmxvZwO0O0OO0O0O.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.csdn.net/tags/MtTakgzsMjE0NTMtYmxvZwO0O0OO0O0O.html" ref="nofollow noopener noreferrer">c 语言命名</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.csdn.net%2Ftags%2FMtTakg1sODc4NDEtYmxvZwO0O0OO0O0O.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.csdn.net/tags/MtTakg1sODc4NDEtYmxvZwO0O0OO0O0O.html" ref="nofollow noopener noreferrer">c 语言变量命名</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.csdn.net%2Ftags%2FMtTaEg0sMzcxMzQtYmxvZwO0O0OO0O0O.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.csdn.net/tags/MtTaEg0sMzcxMzQtYmxvZwO0O0OO0O0O.html" ref="nofollow noopener noreferrer">c 语言教程</a></p>
<p>版权声明：本文为博主原创文章，遵循 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-sa%2F4.0%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://creativecommons.org/licenses/by-sa/4.0/" ref="nofollow noopener noreferrer">CC 4.0 BY-SA</a> 版权协议，转载请附上原文出处链接和本声明。</p>
<p>本文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FZhaDeNianQu%2Farticle%2Fdetails%2F119268000" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ZhaDeNianQu/article/details/119268000" ref="nofollow noopener noreferrer">blog.csdn.net/ZhaDeNianQu…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Feditor.csdn.net%2Fmd%3FarticleId%3D119268000" target="_blank" rel="nofollow noopener noreferrer" title="https://editor.csdn.net/md?articleId=119268000" ref="nofollow noopener noreferrer">编辑</a> 版权</p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6990877365991637022#1%E5%B1%9E%E6%80%A7%E9%83%A8%E5%88%86" title="#1%E5%B1%9E%E6%80%A7%E9%83%A8%E5%88%86" target="_blank">1.属性部分</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#2%E7%B1%BB%E5%9E%8B%E9%83%A8%E5%88%86" title="#2%E7%B1%BB%E5%9E%8B%E9%83%A8%E5%88%86" target="_blank">2.类型部分</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#3%E6%8F%8F%E8%BF%B0%E9%83%A8%E5%88%86" title="#3%E6%8F%8F%E8%BF%B0%E9%83%A8%E5%88%86" target="_blank">3.描述部分</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#4MFC%E3%80%81%E5%8F%A5%E6%9F%84%E3%80%81%E6%8E%A7%E4%BB%B6%E5%8F%8A%E7%BB%93%E6%9E%84%E7%9A%84%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83" title="#4MFC%E3%80%81%E5%8F%A5%E6%9F%84%E3%80%81%E6%8E%A7%E4%BB%B6%E5%8F%8A%E7%BB%93%E6%9E%84%E7%9A%84%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83" target="_blank">4.MFC、句柄、控件及结构的命名规范</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#5%E5%8F%98%E9%87%8F%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83" title="#5%E5%8F%98%E9%87%8F%E5%91%BD%E5%90%8D%E8%A7%84%E8%8C%83" target="_blank">5.变量命名规范</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#6%E5%BA%93%E6%A0%87%E8%AF%86%E7%AC%A6%E5%91%BD%E5%90%8D%E6%B3%95" title="#6%E5%BA%93%E6%A0%87%E8%AF%86%E7%AC%A6%E5%91%BD%E5%90%8D%E6%B3%95" target="_blank">6.库标识符命名法</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#7%E4%B8%BE%E4%BE%8B" title="#7%E4%B8%BE%E4%BE%8B" target="_blank">7.举例</a></li>
<li><a href="https://juejin.cn/post/6990877365991637022#8%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#8%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">8.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7446.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7446.html" ref="nofollow noopener noreferrer">匈牙利命名法</a>是一种编程时的命名规范。<strong>基本原则是：变量名=属性+类型+对象描述</strong>，其中每一对象的名称都要求有明确含义，可以取对象名字全称或名字的一部分。要基于容易记忆容易理解的原则。保证名字的连贯性是非常重要的。</p>
<h2 data-id="heading-1">1.<strong>属性部分</strong></h2>
<pre><code class="copyable">g_   全局变量
c_ 　常量
m_ 　c++类成员变量
s_ 　静态变量
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.<strong>类型部分</strong></h2>
<pre><code class="copyable">数组     a
指针     p
长指针   Long Pointer
函数     fn
无效     v
句柄     h
长整型   l
布尔     b
浮点型（有时也指文件）　f
双字     dw
字符串　 sz
短整型　 n
双精度浮点　d
计数　   c（通常用cnt）
字符　   ch（通常用c）
整型　   i（通常用n）
字节　   by
字　     w
实型　   r
无符号　 u
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3.<strong>描述部分</strong></h2>
<pre><code class="copyable">最大　    Max
最小　    Min
初始化　  Init
临时变量　T（或Temp）
源对象　  Src
目的对象　Dest
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.MFC、句柄、控件及结构的命名规范</h2>
<pre><code class="copyable">Windows类型 样本变量 MFC类 样本变量
HWND hWnd CWnd* pWnd
HDLG hDlg CDialog* pDlg
HDC hDC CDC* pDC
HGDIOBJ hGdiObj CGdiObject* pGdiObj
HPEN hPen CPen* pPen
HBRUSH hBrush CBrush* pBrush
HFONT hFont CFont* pFont
HBITMAP hBitmap CBitmap* pBitmap
HPALETTE hPaltte CPalette* pPalette
HRGN hRgn CRgn* pRgn
HMENU hMenu CMenu* pMenu
HWND hCtl CState* pState
HWND hCtl CButton* pButton
HWND hCtl CEdit* pEdit
HWND hCtl CListBox* pListBox
HWND hCtl CComboBox* pComboBox
HWND hCtl CScrollBar* pScrollBar
HSZ hszStr CString pStr
POINT pt CPoint pt
SIZE size CSize size
RECT rect CRect rect
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5.变量命名规范</h2>
<pre><code class="copyable">ch char 8位字符 chGrade
ch TCHAR 如果_UNICODE定义，则为16位字符 chName
b BOOL 布尔值 bEnable
n int 整型（其大小依赖于操作系统） nLengt
n UINT 无符号值（其大小依赖于操作系统） nHeight
w WORD 16位无符号值 wPos
l LONG 32位有符号整型 lOffset
dw DWORD 32位无符号整型 dwRange
p * 指针 pDoc
lp FAR* 远指针 lpszName
lpsz LPSTR 32位字符串指针 lpszName
lpsz LPCSTR 32位常量字符串指针 lpszName
lpsz LPCTSTR 如果_UNICODE定义，则为32位常量字符串指针 lpszName
h handle Windows对象句柄 hWnd
lpfn callback 指向CALLBACK函数的远指针
前缀 符号类型 实例 范围
IDR_ 不同类型的多个资源共享标识 IDR_MAIINFRAME 1～0x6FFF
IDD_ 对话框资源 IDD_SPELL_CHECK 1～0x6FFF
HIDD_ 对话框资源的Help上下文 HIDD_SPELL_CHECK 0x20001～0x26FF
IDB_ 位图资源 IDB_COMPANY_LOGO 1～0x6FFF
IDC_ 光标资源 IDC_PENCIL 1～0x6FFF
IDI_ 图标资源 IDI_NOTEPAD 1～0x6FFF
ID_ 来自菜单项或工具栏的命令 ID_TOOLS_SPELLING 0x8000～0xDFFF
HID_ 命令Help上下文 HID_TOOLS_SPELLING 0x18000～0x1DFFF
IDP_ 消息框提示 IDP_INVALID_PARTNO 8～0xDEEF
HIDP_ 消息框Help上下文 HIDP_INVALID_PARTNO 0x30008～0x3DEFF
IDS_ 串资源 IDS_COPYRIGHT 1～0x7EEF
IDC_ 对话框内的控件 IDC_RECALC 8～0xDEEF
应用程序符号命名规范

Microsoft MFC宏命名规范:

名称 类型
_AFXDLL 唯一的动态连接库（Dynamic Link Library，DLL）版本
_ALPHA 仅编译DEC Alpha处理器
_DEBUG 包括诊断的调试版本
_MBCS 编译多字节字符集
_UNICODE 在一个应用程序中打开Unicode
AFXAPI MFC提供的函数
CALLBACK 通过指针回调的函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">6.库标识符命名法</h2>
<pre><code class="copyable">标识符 值和含义
u ANSI（N）或Unicode（U）
d 调试或发行：D = 调试，忽略标识符为发行。
静态库版本命名规范:

库 描述
NAFXCWD.LIB 调试版本：MFC静态连接库
NAFXCW.LIB 发行版本：MFC静态连接库
UAFXCWD.LIB 调试版本：具有Unicode支持的MFC静态连接库
UAFXCW.LIB 发行版本：具有Unicode支持的MFC静态连接库
动态连接库命名规范:

名称 类型
_AFXDLL 唯一的动态连接库（DLL）版本
WINAPI Windows所提供的函数
Windows.h中新的命名规范:

类型 定义描述
WINAPI 使用在API声明中的FAR PASCAL位置，如果正在编写一个具有导出API人口点的DLL，则可以在自己的API中使用该类型
CALLBACK 使用在应用程序回叫例程，如窗口和对话框过程中的FAR PASCAL的位置
LPCSTR 与LPSTR相同，只是LPCSTR用于只读串指针，其定义类似（const char FAR*）
UINT 可移植的无符号整型类型，其大小由主机环境决定（对于Windows NT和Windows 9x为32位）；它是unsigned int的同义词
LRESULT 窗口程序返回值的类型
LPARAM 声明lParam所使用的类型，lParam是窗口程序的第四个参数
WPARAM 声明wParam所使用的类型，wParam是窗口程序的第三个参数
LPVOID 一般指针类型，与（void *）相同，可以用来代替LPSTR
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">7.举例</h2>
<pre><code class="copyable">hwnd ：        h 是类型描述，表示句柄， wnd 是变量对象描述，表示窗口，所以 hwnd 表示窗口句柄；
pfnEatApple ： pfn 是类型描述，表示指向函数的指针， EatApple 是变量对象描述，所以它表示指向 EatApple 函数的函数指针变量。
g_cch ：       g_ 是属性描述，表示全局变量，c 和 ch 分别是计数类型和字符类型，一起表示变量类型，这里忽略了对象描述，所以它表示一个对字符进行计数的全局变量。

MFC、句柄、控件及结构的命名规范：
Windows类型 样本变量；MFC类 样本变量
HWND hWnd；
CWnd* pWnd；
HDLG hDlg；
CDialog* pDlg；
HDC hDC；
CDC* pDC；
HGDIOBJ hGdiObj；
CGdiObject* pGdiObj；
HPEN hPen；
CPen* pPen；
HBRUSH hBrush；
CBrush* pBrush；
HFONT hFont；
CFont* pFont；
HBITMAP hBitmap；
CBitmap* pBitmap；
HPALETTE hPaltte；
CPalette* pPalette；
HRGN hRgn；
CRgn* pRgn；
HMENU hMenu；
CMenu* pMenu；
HWND hCtl；
CState* pState；
HWND hCtl；
CButton* pButton；
HWND hCtl；
CEdit* pEdit；
HWND hCtl；
CListBox* pListBox；
HWND hCtl；
CComboBox* pComboBox；
HWND hCtl；
CScrollBar* pScrollBar；
HSZ hszStr；
CString pStr；
POINT pt；
CPoint pt；
SIZE size；
CSize size；
RECT rect；
CRect rect；
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">8.猜你喜欢</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">安装 Visual Studio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7280.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7280.html" ref="nofollow noopener noreferrer">安装 Visual Studio 插件 Visual Assist</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer">Visual Studio 2008 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">Visual Studio 2003/2015 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7284.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7284.html" ref="nofollow noopener noreferrer">设置 Visual Studio 字体/背景/行号</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7387.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7387.html" ref="nofollow noopener noreferrer">C 语言 Hello World</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7404.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7404.html" ref="nofollow noopener noreferrer">C 语言代码注释</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7409.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7409.html" ref="nofollow noopener noreferrer">C 语言数据类型 / 变量类型</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7426.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7426.html" ref="nofollow noopener noreferrer">C 语言变量声明和定义</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7446.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7446.html" ref="nofollow noopener noreferrer">变量命名 – 匈利亚命名法则</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7446.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7446.html" ref="nofollow noopener noreferrer">变量命名 – 匈利亚命名法则</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            