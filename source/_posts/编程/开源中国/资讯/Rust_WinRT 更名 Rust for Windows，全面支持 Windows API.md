
---
title: 'Rust_WinRT 更名 Rust for Windows，全面支持 Windows API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6337'
author: 开源中国
comments: false
date: Tue, 11 May 2021 23:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6337'
---

<div>   
<div class="content">
                                                                    
                                                        <p>微软已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.windows.com%2Fwindowsdeveloper%2F2021%2F05%2F06%2Fannouncing-rust-for-windows-v0-9%2F" target="_blank">宣布推出</a> Rust for Windows v0.9，其中包括完全的 consumption 支持 ，以及其他一些更新内容。该版本发布后，Rust 开发者将能够以一种更加习惯的方式，访问完整的 Windows API，从而轻松构建功能强大且丰富的 Windows 应用程序。 </p> 
<p>微软曾于去年 5 月推出了 Rust for Windows（以前叫 Rust/WinRT）的早期预览版。该项目和 C++/WinRT 一脉相承，用标准语言和编译器为 Windows 运行时构建语言投影，从而方便 Rust 开发人员调用 Windows API，更轻松地使用 Rust 构建各类 Windows 应用和组件。</p> 
<p>v0.9 中包含的一些更新内容包括有：</p> 
<ul> 
 <li>添加了对 Win32 和 COM API 的支持，统一了可通过  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Fwindows" target="_blank">Windows</a> crate 使用的 Windows API。这些 API 的添加由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fwin32metadata" target="_blank">win32metadata</a> 项目启用。随着 Windows API 覆盖面的扩大和统一，项目名称也从“Rust/WinRT”更改为“Rust for Windows”。</li> 
 <li>在 Rust for Windows 存储库中添加了几个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fwindows-rs%2Ftree%2Fmaster%2Fexamples" target="_blank">示例</a>，演示了如何调用各种 Windows API（包括 Win32、COM 和 WinRT API）。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Fwindows" target="_blank">Windows</a> crate 发布在 crates.io 上，现在已经获得了 MIT 或 Apache 的双重许可。 </li> 
 <li>Windows crate 现在使用生成的绑定，而不是内部手写的绑定。</li> 
 <li>Windows crate 现在可以在 Linux 上构建。</li> 
 <li>Win32 API 的许多改进和修复，例如对数组类型、各种字符串类型和更新的元数据的支持。 </li> 
 <li>添加了对 COM 接口的更自然和惯用的支持，例如带返回值，以及对涉及 C-style unions 和嵌套类型的额外 API 的支持。</li> 
 <li>缩短了构建时间并改善了错误处理。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fwindows-rs%2Fpull%2F646" target="_blank">保留了</a> Original API case，这将影响使用 Windows crate 的现有代码。</li> 
 <li>将类似于 QueryInterface 的函数转换为通用函数，从而可以更安全、更方便地调用许多与 COM 相关的函数。</li> 
</ul> 
<p>详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.windows.com%2Fwindowsdeveloper%2F2021%2F05%2F06%2Fannouncing-rust-for-windows-v0-9%2F" target="_blank">发布公告</a>。</p> 
<p><strong>延伸阅读：</strong><a href="https://www.oschina.net/news/115354/microsoft-winrt" target="_blank">微软开源 Rust/WinRT，方便使用 Rust 构建 Windows 应用</a></p>
                                        </div>
                                      
</div>
            