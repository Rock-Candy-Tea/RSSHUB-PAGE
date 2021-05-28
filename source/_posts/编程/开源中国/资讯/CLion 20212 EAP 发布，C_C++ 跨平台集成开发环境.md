
---
title: 'CLion 2021.2 EAP 发布，C_C++ 跨平台集成开发环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-49e4c07b1608343a91ecc1343fcf09265ee.gif'
author: 开源中国
comments: false
date: Fri, 28 May 2021 07:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-49e4c07b1608343a91ecc1343fcf09265ee.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CLion 2021.2 EAP 现已发布。该 EAP 版本是免费使用的，但是可能不稳定且质量较低，其主要目的是让用户评估即将被添加到下一个版本的功能，并在早期阶段分享他们的反馈。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li><strong>CMake 增强</strong> 
  <ul> 
   <li>CLion 现在捆绑并支持 CMake 3.20 ，该版本包括 CMake 预设、对 CMake 文件 API 的重大更新、对 C++23 编译器模式的支持以及针对 CUDA 开发者的更新。</li> 
   <li> <p>CLion 使用 CMake Profiles 来进行配置，且现在支持从 CMake 预设中导入信息。不过，目前导入的预设是只读的，且只支持 buildPresets 预设。导入后，CLion 中 的 CMake 预设会得到一个指向 CLion 工具链的链接。</p> </li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-49e4c07b1608343a91ecc1343fcf09265ee.gif" referrerpolicy="no-referrer"></li> 
   <li>除了新的 CMakeList.txt 文件模板外，CLion 现在还为 CMake 项目提供了可编辑的模板。用户可以在 Settings/Preferences | Editor | File and Code Templates | Other 找到它。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-e67377fe25c492e30600865698bc9d1f67d.png" referrerpolicy="no-referrer"></li> 
   <li>在 Run/Debug 配置的 "Before Launch" 部分，用户可以指定在启动所选目标之前要执行的任务，现在用户还可以在这个阶段添加一个 CMake 目标任务来执行 CMake 目标。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-05dcab441d02f20e129c3771efd4fe83869.png" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
 <li><strong>生存周期分析</strong> 
  <ul> 
   <li>CLion 现在支持生存周期分析，例如 CLion 会警告用户，在临时字符串被销毁后，字符串视图引用了一个无效的对象。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-02b40b76b6200a90750034eb041f0fe85c8.png" referrerpolicy="no-referrer"></li> 
   <li>CLion 也会捕捉到各种局部变量指向超出范围的内存的情况。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-733ff7c5f17f9450cbba1f0ccfccfa616c7.png" referrerpolicy="no-referrer"></li> 
   <li>分析还支持 GSL 注释。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-5068f21427f6bd4582af2fc4743d683bd32.png" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
 <li><strong>Cling 支持</strong> 
  <ul> 
   <li>CLion 现在支持交互式的 C++ 解释器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Froot-project%2Fcling" target="_blank">Cling</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Froot-project%2Fcling" target="_blank">Cling</a> 建立在 Clang 和 LLVM 基础之上，对原型设计和学习 C++ 非常有用。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-5f6a96381d044e00de269e674026b425596.png" referrerpolicy="no-referrer"></li> 
   <li>支持将当前代码行发送到 Cling 会话。</li> 
   <li><img alt src="https://oscimg.oschina.net/oscnet/up-82b723be6f6288209f5faf4c39a72f8e029.png" referrerpolicy="no-referrer"></li> 
   <li>不过，用户暂时不能从 CLion 内部开始向 Cling 可执行文件添加额外的参数，所以无法真正改变 C++ 语言标准或其他选项。另外，Cling 会话在项目目录或主目录内启动（如果当前没有打开项目）。当从一个不在项目根目录下的文件向 Cling 发送当前行时，相对路径可能会出错。</li> 
  </ul> </li> 
 <li><strong>WSL 增强</strong> 
  <ul> 
   <li>Clion 现在使用专门的 WSL API 启动 WSL，这使得配置 WSL 更加容易。而且不仅支持从微软商店安装的 WSL，而且还支持从自定义发行版安装的WSL。</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fclion%2F2021%2F05%2Fclion-starts-2021-2-eap-presets-cling-lifetimes%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            