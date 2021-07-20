
---
title: 'ReSharper C++ 2021.2 EAP 发布，支持类型转换提示'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9ab4841f6d421779a1dd1674c2abe8676c5.png'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 06:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9ab4841f6d421779a1dd1674c2abe8676c5.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ReSharper C++ 2021.2 EAP 现已发布。该版本结束了 2021.2 开发周期，并带来了路线图中概述的其余功能。像往常一样，EAP 版本可以免费使用，并可从官方网站或通过 Toolbox 应用程序下载。以下是主要更新内容：</p> 
<h4>类型转换提示</h4> 
<p>该版本引入了一种新的 inlay 提示 —— 类型转换提示。类型转换提示有助于隐式转换可见，以便开发者了解潜在的性能和正确性影响。与其他 inlay 提示类似，开发者可以在专用设置页面上配置类型转换提示。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9ab4841f6d421779a1dd1674c2abe8676c5.png" referrerpolicy="no-referrer"></p> 
<p>默认情况下，开发者将看到用于隐式转换的特殊图标，也可以切换到更详细但也更易读的显示模式。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-77109e7930d4e8db2d2b047ba12351b780f.png" referrerpolicy="no-referrer"></p> 
<p>该功能还支持排除列表，可让开发者隐藏代码库中特定类的隐式转换。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b24ac98f34ce065927da5efd2bb608d0ea5.gif" referrerpolicy="no-referrer"></p> 
<h4>不变性检查</h4> 
<p>该版本并引入了两项不变性相关的新检查。第一个检查扩展了对引用和指针类型的函数参数的不变性分析，并且默认情况下，将指针和引用传递给常量。遵循此规则可确保函数不会修改通过引用或指针传递的参数。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-efae5782d9f20cbdcd0ccc7d36472570425.gif" referrerpolicy="no-referrer"></p> 
<p>第二个检查可以在编译时使用 constexpr 评估的变量，将 constexpr 用于可以在编译时计算的值，这可以带来更好的性能和更好的编译时检查。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b1de58df40a6c566802f8f8261e82651d77.gif" referrerpolicy="no-referrer"></p> 
<h4>原始字符串文字</h4> 
<p>开发者现在可以使用新的上下文操作将任何字符串转换为 C++11 原始字符串文字，这样更易​​于阅读。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-694ff7d8c3c93e717e52589fe77caa9115d.gif" referrerpolicy="no-referrer"></p> 
<p>这种转换是双向的，因此开发者也可以将原始字符串文字转换为常规字符串文字。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a8981fd1058c63995ef01ad6a2f9abfcbdc.gif" referrerpolicy="no-referrer"></p> 
<h4>在退格时取消缩进</h4> 
<p>当开发者在空行或插入符左侧有空格和制表符时按 Backspace 时，ReSharper C++ 现在可以将插入符放置在适当的缩进位置，而不是一次将其移回一个位置。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-82cc621a8708bce8da4b537a971265c3a51.gif" referrerpolicy="no-referrer"></p> 
<h4>指向 cppreference.com 的嵌入式链接</h4> 
<p>现在可以使用快速文档弹出窗口中的阅读更多链接 (Ctrl+Shift+F1) 在浏览器中打开 cppreference.com 中有关标准库类或函数详细信息的相应页面。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1558b3bb00dc9fa1383b4450575d7c11467.gif" referrerpolicy="no-referrer"></p> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Frscpp%2F2021%2F07%2F19%2Fresharper-cpp-2021-2-eap-type-conversion-hints-immutability-inspections%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            