
---
title: 'JSON for Modern C++ 3.10.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4780'
author: 开源中国
comments: false
date: Mon, 23 Aug 2021 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4780'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JSON for Modern C++ 3.10.0<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.10.0" target="_blank"> 已发布</a>，这是推出 <a href="https://www.oschina.net/news/117737/json-for-modern-cpp-3-9-1-released" target="_blank">3.9.1</a> 一年多后的首次更新。此版本增加了一些新功能、引入许多小的变化和修复错误。</p> 
<p>其中值得注意的变化是增加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fhome%2Fexceptions%2F%23extended-diagnostic-messages" target="_blank">扩展的诊断功能</a>，通过在引入<code>json.hpp</code>之前定义<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Ffeatures%2Fmacros%2F%23json_diagnostics" target="_blank"><code>JSON_DIAGNOSTICS</code></a>，JSON 指针会被添加到异常中，这有助于调试对象访问、数组索引或类型不匹配的问题。</p> 
<p>另一个重要变化是增加完全超负荷工作的 CI，它会对每次 commit 执行大量检查，支持将来更频繁地发布新版本。</p> 
<h3>新功能</h3> 
<ul> 
 <li> <p>通过向<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fhome%2Fexceptions%2F" target="_blank">异常</a>消息添加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc6901" target="_blank">JSON 指针</a>来添加<strong>可扩展的诊断信息</strong>，指示无效类型错误或越界错误的确切位置。</p> 
  <div> 
   <pre><span style="background-color:var(--color-bg-tertiary)"><code> [json.exception.type_error.302] (/address/housenumber) type must be number, but is string
</code></span></pre> 
  </div> <p>库会在检测到的 JSON 值的本地上下文中抛出异常。此操作对于获取详细的诊断信息以及进行调试都比较困难。为了创建更好的诊断信息，每个 JSON 值都需要一个指向其父值的指针，以便可以创建全局上下文（即从根值到导致异常的值的路径）。然后将该全局上下文作为 JSON 指针提供。由于使用此全局上下文的代价是为每个 JSON 值存储一个额外的指针以及维护父关系的运行时开销，因此默认情况下会禁用扩展诊断。参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fhome%2Fexceptions%2F%23extended-diagnostic-messages" target="_blank">文档</a>了解更多信息。</p> </li> 
 <li> <p>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Ftree%2Fdevelop%2Fthird_party%2Fgdb_pretty_printer" target="_blank"><strong>GDB pretty printer</strong></a> 以方便读取 GDB 中的<code>basic_json</code>值</p> </li> 
 <li> <p>添加新的<code>store</code>值到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson.nlohmann.me%2Fapi%2Fbasic_json%2Fcbor_tag_handler_t%2F" target="_blank">cbor_tag_handler_t</a>，它可以将 CBOR 值的标签存储为二进制子类型</p> </li> 
 <li> <p>添加对具有不可默认构造类型的容器的支持</p> </li> 
</ul> 
<h3 style="text-align:start"><span style="color:#24292e"><span style="background-color:#ffffff">错误修复</span></span></h3> 
<ul> 
 <li>修复<code>ordered_json</code>关闭异常时无法使用的回归错误</li> 
 <li>为<code>ordered_json</code>增加了迭代器范围插入</li> 
 <li>将二进制子类型的类型更改为<code>std::uint64_t</code>，如果没有给出子类型，<code>subtype()</code>函数的返回值已修复为文档值<code>-1</code></li> 
 <li>修复内部<code>json_ref</code>类型的移动构造函数，该构造函数在使用<code>-fno-elide-constructors</code>进行编译时会创建<code>null</code>值</li> 
 <li>修复容器在边缘情况下的<code>input_adapter</code>编译问题</li> 
 <li>支持从<code>std::byte</code>容器进行解析</li> 
 <li>在<code>to_json</code>重用 JSON 值的情况下修复内存泄漏问题</li> 
 <li>在<code>EOF</code>找不到符号的情况下修复编译错误</li> 
 <li>修复在 libc++ 上使用<code>NLOHMANN_JSON_SERIALIZE_ENUM</code>搭配<code>ordered_json</code>时的编译错误</li> 
</ul> 
<p>所有变更均向后兼容，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnlohmann%2Fjson%2Freleases%2Ftag%2Fv3.10.0" target="_blank">点此查看完整更新内容</a>。</p>
                                        </div>
                                      
</div>
            