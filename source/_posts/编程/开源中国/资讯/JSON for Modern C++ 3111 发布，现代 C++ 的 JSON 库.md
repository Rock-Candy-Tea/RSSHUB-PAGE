
---
title: 'JSON for Modern C++ 3.11.1 发布，现代 C++ 的 JSON 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6559'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6559'
---

<div>   
<div class="content">
                                                                                            <p>JSON for Modern C++ 3.11.1 现已发布，具体更新内容包括：</p> 
<p><strong>Known issues</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3652" target="_blank">#3652</a> Regression：对 member function“value”的调用不明确</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3654" target="_blank">#3654</a> Regression：比较 json_pointer 和 const char */string_t 的'operator!='不匹配</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3655" target="_blank">#3655</a> Regression：.value<size_t> 存在编译错误</li> 
</ul> 
<p>所有问题都在分支中得到修复，并将成为 3.11.2 版本的一部分。</p> 
<p><strong>Summary</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.11.0" target="_blank"><span style="color:#24292f">版本 3.11.0</span></a><span style="color:#24292f"> 将 user-defined string literals (UDL) 移至命名空间<code>nlohmann::literals::json_literals</code>（可参阅</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fmacros%2Fjson_use_global_udls%2F" target="_blank"><span style="color:#24292f">文档</span></a><span style="color:#24292f">）。但默认情况下，这个命名空间没有被导入到全局命名空间，这破坏了代码。此版本修复了此错误。</span></p> 
<p><span style="color:#24292f">所有更改都是向后兼容的。有关其他功能的更多信息，参阅</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.11.0" target="_blank"><span style="color:#24292f">版本 3.11.0的发行说明。</span></a></p> 
<p><strong>Bug fixes</strong></p> 
<ul> 
 <li>将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fmacros%2Fjson_use_global_udls%2F" target="_blank"><code>JSON_USE_GLOBAL_UDLS</code></a>的默认值和 CMake 选项<code>JSON_GlobalUDLs</code>设置为 1，以默认将 user-defined string literals 从<code>nlohmann::literals::json_literals</code>命名空间导入全局命名空间中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3644" target="_blank">#3644 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3645" target="_blank">#3645 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3646" target="_blank">#3646</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.11.1" target="_blank">https://github.com/nlohmann/json/releases/tag/v3.11.1</a></p>
                                        </div>
                                      
</div>
            