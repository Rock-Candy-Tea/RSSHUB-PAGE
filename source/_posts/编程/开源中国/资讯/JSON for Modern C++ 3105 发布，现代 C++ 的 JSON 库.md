
---
title: 'JSON for Modern C++ 3.10.5 发布，现代 C++ 的 JSON 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7996'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7996'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0"><span style="color:#000000">JSON for Modern C++  3.10.5 发布了，它</span>在 C++ 下使用的 JSON 库。</p> 
   <p style="margin-left:0; margin-right:0">去年 10 月的 3.10.4 版本引入了将<span> </span><code><strong>std::filesystem</strong></code><span> </span>对象和 JSON 相互转换的功能支持，当时是<span style="color:#24292f">假设任何支持 C++17 的编译器都会有适当的文件系统支持，但现在看来并非如此。因此在最新的 3.10.5 版本引入了预处理器检查（以及对应方法），确保在检测到编译器支持此功能时才编译转换。</span></p> 
   <p style="margin-left:0; margin-right:0"><span style="color:#24292f">完整更新内容如下：</span></p> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>Bug 修复</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><span style="color:#24292f">确保<strong>仅在编译器支持时</strong>才使用 C++17 文件系统转换。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3090" target="_blank">#3090<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3097" target="_blank">#3097<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3101" target="_blank">#3101<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3156" target="_blank">#3156<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3203" target="_blank">#3203</a></li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">（将<span> </span><code>JSON_HAS_FILESYSTEM</code><span> </span>和<span> </span><code>JSON_HAS_EXPERIMENTAL_FILESYSTEM</code><span> </span>设置为 0 ，可以完全不使用此功能）</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><span style="color:#24292f">修复 Nvidia CUDA Compiler (NVCC) 的编译错误。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3013" target="_blank">#3013<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3234" target="_blank">#3234</a></li> 
   </ul> 
   <h4 style="margin-left:.6em; margin-right:0"><strong>Warnings</strong></h4> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复阴影变量的警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3188" target="_blank">#3188<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3193" target="_blank">#3193</a></li> 
    <li>修复无意义的比较导致的警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3227" target="_blank">#3227<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F2712" target="_blank">#2712<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F2676" target="_blank">#2676<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F1390" target="_blank">#1390<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F755" target="_blank">#755</a></li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0">改进</h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>向<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fbasic_json%2Fupdate%2F" target="_blank"><code>update</code></a><span> </span>函数添加参数，以递归地合并具有公共键的对象。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fdiscussions%2F3006" target="_blank">#3006<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3069" target="_blank">#3069</a></li> 
    <li><span style="color:#24292f">扩展  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fbasic_json%2Fstd_hash%2F%23version-history" target="_blank"><code>std::hash</code></a><span style="color:#24292f"><span> </span>和<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fbasic_json%2Fstd_swap%2F" target="_blank"><code>std::swap</code></a><span style="color:#24292f"><span> </span>以专门为<span> </span></span><code>nlohmann::basic_json</code><span style="color:#24292f"><span> </span>工作，而不限于<span> </span></span><code>nlohmann::json</code><span> </span>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3121" target="_blank">#3121</a></li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0">其他变更</h3> 
   <p style="margin-left:0; margin-right:0"><strong>测试和 CI</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>更新 CI 以使用 Clang 14、GCC 6 和 Clang-Tidy 14  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3088" target="_blank">#3088</a></li> 
    <li>更新 cpplint。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3225" target="_blank">#3225</a></li> 
    <li><span style="color:#24292f">为 Nvidia CUDA 编译器 (NVCC) 添加构建步骤。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3227" target="_blank">#3227</a></li> 
    <li><span style="color:#24292f">删除 Travis CI。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3087" target="_blank">#3087<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3233" target="_blank">#3233</a></li> 
    <li>使用 C++17 编译并执行测试套件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3101" target="_blank">#3101</a></li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">此外还有一些文档变更，细节可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.10.5" target="_blank">https://github.com/nlohmann/json/releases/tag/v3.10.5</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            