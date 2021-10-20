
---
title: 'JSON for Modern C++  3.10.4 发布，主要修复 3.10.0 版本 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1059'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1059'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">JSON for Modern C++  3.10.4 发布了，主要修复了 3.10.0 版本带来的两个 bug ，此次的更新内容均向后兼容。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复 bug</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">修复版本 3.10.0 中引入的回归错误，这个错误导致了：带默认参数的显式构造函数在编译时会报错。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3077" target="_blank">#3077<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3079" target="_blank">#3079</a></li> 
 <li><span style="color:#24292f">修复版本 3.10.0 中引入的回归错误，这个错误导致了：</span><code>std::find</code><span style="color:#24292f"><span> </span>和<span> </span></span><code>std::remove</code><span style="color:#24292f"><span> </span>的返回值被当成一个指针，在编译时会出错<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3081" target="_blank">#3081<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3082" target="_blank">#3082</a></li> 
 <li>修复<span> </span><code>std::filesystem::path</code><span style="color:#24292f"><span> </span>转换 JSON 的问题，在 3.10.3 版本之前，这种转换会导致栈溢出，3.10.3 版本在Windows 系统的编译更糟糕。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fissues%2F3070" target="_blank">#3070<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Fpull%2F3073" target="_blank">#3073</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>弃用函数</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">不建议通过初始化列表的方式将迭代器对组或指针/长度对组传递到解析函数<span style="color:#24292f">(</span><code>basic_json::parse</code><span style="color:#24292f">,<span> </span></span><code>basic_json::accept</code><span style="color:#24292f">,<span> </span></span><code>basic_json::sax_parse</code><span style="color:#24292f">,<span> </span></span><code>basic_json::from_cbor</code><span style="color:#24292f">,<span> </span></span><code>basic_json::from_msgpack</code><span style="color:#24292f">,<span> </span></span><code>basic_json::from_ubjson</code><span style="color:#24292f">,<span> </span></span><code>basic_json::from_bson</code><span style="color:#24292f">) 。</span>应当传递两个迭代器，例如，调用<span> </span><code>basic_json::from_cbor(ptr, ptr+len)</code><span> </span>而不是<span> </span><code>basic_json::from_cbor(&#123;ptr, len&#125;)</code></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">以下函数在早期版本中已被弃用，并将在下一个主要版本（ 4.0.0）中删除：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>iterator_wrapper</code><span> </span>已弃用。请改用成员函数<code>items()</code>。</li> 
 <li>功能<span> </span><code>friend std::istream& operator<<(basic_json&, std::istream&)</code>和<code>friend std::ostream& operator>>(const basic_json&, std::ostream&)</code>已弃用。请使用<code>friend std::istream& operator>>(std::istream&, basic_json&)</code>和<code>friend operator<<(std::ostream&, const basic_json&)</code>代替。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">所有弃用都带有注释<span> </span><code><u>HEDLEY_DEPRECATED_FOR</u></code></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.10.4" target="_blank">https://github.com/nlohmann/json/releases/tag/v3.10.4</a></p>
                                        </div>
                                      
</div>
            