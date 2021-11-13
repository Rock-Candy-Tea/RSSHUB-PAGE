
---
title: 'Java 和 C# 最大的不同是什么？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=7605'
author: 知乎
comments: false
date: Fri, 12 Nov 2021 18:27:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=7605'
---

<div>   
hez2010的回答<br><br><p>我觉得抛开语法而谈，最主要的还是对底层的控制能力不同。</p><p>C# 一开始虽然借鉴 Java，但是目的完全不是为了造一个 better Java，而是造一个 better C++。游戏引擎们偏爱 C# 也是有这一层原因在里面，这一点高赞回答中 <a class="member_mention" href="http://www.zhihu.com/people/14d8617e8527b4b36c5d95afa0c4242b" data-hash="14d8617e8527b4b36c5d95afa0c4242b" data-hovercard="p$b$14d8617e8527b4b36c5d95afa0c4242b">@MaxwellGeng</a> 的回答已经足够能说清了。</p><p><br></p><p>比如在 C# 里面你能干的：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">x</span> <span class="p">=</span> <span class="k">new</span> <span class="kt">int</span><span class="p">[</span><span class="m">10</span><span class="p">];</span>
<span class="k">fixed</span> <span class="p">(</span><span class="kt">int</span><span class="p">*</span> <span class="n">p</span> <span class="p">=</span> <span class="n">x</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(*((</span><span class="kt">long</span><span class="p">*)</span><span class="n">p</span> <span class="p">-</span> <span class="m">1</span><span class="p">));</span> <span class="c1">// 10</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>上述代码会输出 10，为什么？因为 .NET 中数组的长度存储于数组第一个元素之前的 8 字节内存中。如果你再接着输出 <code>*((long*)p - 2)</code>，将会直接得到这个对象的 <code>TypeHandle</code> 地址：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">((</span><span class="kt">long</span><span class="p">)</span><span class="k">typeof</span><span class="p">(</span><span class="kt">int</span><span class="p">[]).</span><span class="n">TypeHandle</span><span class="p">.</span><span class="n">Value</span> <span class="p">==</span> <span class="p">*((</span><span class="kt">long</span><span class="p">*)</span><span class="n">p</span> <span class="p">-</span> <span class="m">2</span><span class="p">));</span> <span class="c1">// True</span>
</span></code></pre></div><p>然后拿着这个指针又接着能去访问对象的 <code>MethodTable</code>。</p><p><br></p><p>再有你还可以手动在栈上分配空间：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">x</span> <span class="p">=</span> <span class="k">stackalloc</span> <span class="kt">int</span><span class="p">[</span><span class="m">2</span><span class="p">];</span> <span class="c1">// 或者 Span<int> x = stackalloc int[2]; 做安全访存</span>
<span class="n">x</span><span class="p">[</span><span class="m">0</span><span class="p">]</span> <span class="p">=</span> <span class="m">3</span><span class="p">;</span>
<span class="n">x</span><span class="p">[</span><span class="m">1</span><span class="p">]</span> <span class="p">=</span> <span class="m">1</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="m">0</span><span class="p">]</span> <span class="p">+</span> <span class="n">x</span><span class="p">[</span><span class="m">1</span><span class="p">]);</span> <span class="c1">// 4</span>
</span></code></pre></div><p><br></p><p>接着你想绕过 GC 直接手动分配堆内存：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">array</span> <span class="p">=</span> <span class="p">(</span><span class="kt">int</span><span class="p">*)</span><span class="n">NativeMemory</span><span class="p">.</span><span class="n">Alloc</span><span class="p">(</span><span class="m">10</span><span class="p">,</span> <span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>
<span class="n">array</span><span class="p">[</span><span class="m">0</span><span class="p">]</span> <span class="p">=</span> <span class="m">1</span><span class="p">;</span>
<span class="n">array</span><span class="p">[</span><span class="m">1</span><span class="p">]</span> <span class="p">=</span> <span class="m">3</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">array</span><span class="p">[</span><span class="m">0</span><span class="p">]</span> <span class="p">+</span> <span class="n">array</span><span class="p">[</span><span class="m">1</span><span class="p">]);</span> <span class="c1">// 4</span>
<span class="n">NativeMemory</span><span class="p">.</span><span class="n">Free</span><span class="p">(</span><span class="n">array</span><span class="p">);</span>
</span></code></pre></div><p>上述调用等价于你在 C 语言中调用的 <code>malloc</code>，此外还有 <code>AllocAligned</code>、<code>Realloc</code>、<code>AllocZeroed</code> 等等，可以直接控制内存对齐。</p><p><br></p><p>接下来你想创建一个显式内存布局的结构 <code>Foo</code>：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">obj</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Foo</span><span class="p">();</span>
<span class="n">obj</span><span class="p">.</span><span class="n">Float</span> <span class="p">=</span> <span class="m">1</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">Int</span><span class="p">);</span> <span class="c1">// 1065353216</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">Bytes</span><span class="p">[</span><span class="m">0</span><span class="p">]);</span> <span class="c1">// 0</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">Bytes</span><span class="p">[</span><span class="m">1</span><span class="p">]);</span> <span class="c1">// 0</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">Bytes</span><span class="p">[</span><span class="m">2</span><span class="p">]);</span> <span class="c1">// 128</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">Bytes</span><span class="p">[</span><span class="m">3</span><span class="p">]);</span> <span class="c1">// 63</span>

<span class="na">[StructLayout(LayoutKind.Explicit)]</span>
<span class="k">struct</span> <span class="nc">Foo</span>
<span class="p">&#123;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">int</span> <span class="n">Int</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">float</span> <span class="n">Float</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="k">unsafe</span> <span class="k">fixed</span> <span class="kt">byte</span> <span class="n">Bytes</span><span class="p">[</span><span class="m">4</span><span class="p">];</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>然后你就成功模拟出了一个 C 的 Union，之所以会有上面的输出，是因为单精度浮点数 1 的二进制表示为 <code>0x00111111100000000000000000000000</code>，以小端方式存储后占 4 个字节，分别是 <code>0x00000000</code>、<code>0x00000000</code>、<code>0x10000000</code>、<code>0x00111111</code>。</p><p><br></p><p>进一步，你还能直接从内存数据没有任何拷贝开销地构造对象：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">data</span> <span class="p">=</span> <span class="k">stackalloc</span> <span class="kt">byte</span><span class="p">[]</span> <span class="p">&#123;</span> <span class="m">0</span><span class="p">,</span> <span class="m">0</span><span class="p">,</span> <span class="m">128</span><span class="p">,</span> <span class="m">63</span> <span class="p">&#125;;</span>
<span class="kt">var</span> <span class="n">foo</span> <span class="p">=</span> <span class="n">Unsafe</span><span class="p">.</span><span class="n">AsRef</span><span class="p"><</span><span class="n">Foo</span><span class="p">>(</span><span class="n">data</span><span class="p">);</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">foo</span><span class="p">.</span><span class="n">Float</span><span class="p">);</span> <span class="c1">// 1</span>

<span class="na">[StructLayout(LayoutKind.Explicit)]</span>
<span class="k">struct</span> <span class="nc">Foo</span>
<span class="p">&#123;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">int</span> <span class="n">Int</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">float</span> <span class="n">Float</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="k">unsafe</span> <span class="k">fixed</span> <span class="kt">byte</span> <span class="n">Bytes</span><span class="p">[</span><span class="m">4</span><span class="p">];</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>从堆内存创建自然也没问题：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">data</span> <span class="p">=</span> <span class="k">new</span> <span class="kt">byte</span><span class="p">[]</span> <span class="p">&#123;</span> <span class="m">0</span><span class="p">,</span> <span class="m">0</span><span class="p">,</span> <span class="m">128</span><span class="p">,</span> <span class="m">63</span> <span class="p">&#125;;</span>
<span class="k">fixed</span> <span class="p">(</span><span class="k">void</span><span class="p">*</span> <span class="n">p</span> <span class="p">=</span> <span class="n">data</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">foo</span> <span class="p">=</span> <span class="n">Unsafe</span><span class="p">.</span><span class="n">AsRef</span><span class="p"><</span><span class="n">Foo</span><span class="p">>(</span><span class="n">p</span><span class="p">);</span>
    <span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">foo</span><span class="p">.</span><span class="n">Float</span><span class="p">);</span> <span class="c1">// 1</span>
<span class="p">&#125;</span>

<span class="na">[StructLayout(LayoutKind.Explicit)]</span>
<span class="k">struct</span> <span class="nc">Foo</span>
<span class="p">&#123;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">int</span> <span class="n">Int</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="kt">float</span> <span class="n">Float</span><span class="p">;</span>
<span class="na">    [FieldOffset(0)]</span> <span class="k">public</span> <span class="k">unsafe</span> <span class="k">fixed</span> <span class="kt">byte</span> <span class="n">Bytes</span><span class="p">[</span><span class="m">4</span><span class="p">];</span>
<span class="p">&#125;</span>
</span></code></pre></div><p><br></p><p>再比如，此时你面前有一个使用 C++ 编写的库，其中有这么一段代码：</p><div class="highlight"><pre><code class="language-cpp"><span><span class="cp">#include</span> <span class="cpf"><cstring></span><span class="cp">
<span class="cp">#include</span> <span class="cpf"><cstdio></span><span class="cp">

<span class="k">extern</span> <span class="s">"C"</span> <span class="kr">__declspec</span><span class="p">(</span><span class="n">dllexport</span><span class="p">)</span>
<span class="kt">char</span><span class="o">*</span> <span class="kr">__cdecl</span> <span class="n">foo</span><span class="p">(</span><span class="kt">char</span><span class="o">*</span> <span class="p">(</span><span class="o">*</span><span class="n">gen</span><span class="p">)(</span><span class="kt">int</span><span class="p">),</span> <span class="kt">int</span> <span class="n">count</span><span class="p">)</span> <span class="p">&#123;</span>
    <span class="k">return</span> <span class="n">gen</span><span class="p">(</span><span class="n">count</span><span class="p">);</span>
<span class="p">&#125;</span>
</span></span></span></code></pre></div><p>然后我们编写如下 C# 代码：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="na">[DllImport("./foo.dll", EntryPoint = "foo"), SuppressGCTransition]</span>
<span class="k">static</span> <span class="k">extern</span> <span class="kt">string</span> <span class="nf">Foo</span><span class="p">(</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">]<</span><span class="kt">int</span><span class="p">,</span> <span class="n">nint</span><span class="p">></span> <span class="n">gen</span><span class="p">,</span> <span class="kt">int</span> <span class="n">count</span><span class="p">);</span>

<span class="na">[UnmanagedCallersOnly(CallConvs = new[]</span> <span class="p">&#123;</span> <span class="k">typeof</span><span class="p">(</span><span class="n">CallConvCdecl</span><span class="p">)</span> <span class="p">&#125;),</span> <span class="n">SuppressGCTransition</span><span class="p">]</span>
<span class="k">static</span> <span class="n">nint</span> <span class="nf">Generate</span><span class="p">(</span><span class="kt">int</span> <span class="n">count</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">str</span> <span class="p">=</span> <span class="n">Enumerable</span><span class="p">.</span><span class="n">Repeat</span><span class="p">(</span><span class="s">"w"</span><span class="p">,</span> <span class="n">count</span><span class="p">).</span><span class="n">Aggregate</span><span class="p">((</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span> <span class="p">=></span> <span class="err">$</span><span class="s">"&#123;a&#125;&#123;b&#125;"</span><span class="p">);</span>
    <span class="k">return</span> <span class="n">Marshal</span><span class="p">.</span><span class="n">StringToHGlobalAnsi</span><span class="p">(</span><span class="n">str</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="kt">var</span> <span class="n">f</span> <span class="p">=</span> <span class="p">(</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">]<</span><span class="kt">int</span><span class="p">,</span> <span class="n">nint</span><span class="p">>)&</span><span class="n">Generate</span><span class="p">;</span>
<span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">Foo</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="m">5</span><span class="p">);</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">result</span><span class="p">);</span> <span class="c1">// wwwww</span>
</span></code></pre></div><p>上面的代码干了什么事情？我们将 C# 的函数指针传到了 C++ 代码中，然后在 C++ 侧调用 C# 函数生成了一个字符串 <code>wwwww</code>，然后将这个字符串返回给 C# 侧。而就算不用函数指针换成使用委托也没有区别，因为 .NET 中的委托下面就是函数指针。</p><p>甚至，如果我们不想让 .NET 导入 <code>foo.dll</code>，我们想自行决定动态库的生命周期，还可以这么写：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="na">[UnmanagedCallersOnly(CallConvs = new[]</span> <span class="p">&#123;</span> <span class="k">typeof</span><span class="p">(</span><span class="n">CallConvCdecl</span><span class="p">)</span> <span class="p">&#125;),</span> <span class="n">SuppressGCTransition</span><span class="p">]</span>
<span class="k">static</span> <span class="n">nint</span> <span class="nf">Generate</span><span class="p">(</span><span class="kt">int</span> <span class="n">count</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">str</span> <span class="p">=</span> <span class="n">Enumerable</span><span class="p">.</span><span class="n">Repeat</span><span class="p">(</span><span class="s">"w"</span><span class="p">,</span> <span class="n">count</span><span class="p">).</span><span class="n">Aggregate</span><span class="p">((</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span> <span class="p">=></span> <span class="err">$</span><span class="s">"&#123;a&#125;&#123;b&#125;"</span><span class="p">);</span>
    <span class="k">return</span> <span class="n">Marshal</span><span class="p">.</span><span class="n">StringToHGlobalAnsi</span><span class="p">(</span><span class="n">str</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="kt">var</span> <span class="n">f</span> <span class="p">=</span> <span class="p">(</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">]<</span><span class="kt">int</span><span class="p">,</span> <span class="n">nint</span><span class="p">>)&</span><span class="n">Generate</span><span class="p">;</span>
<span class="kt">var</span> <span class="n">library</span> <span class="p">=</span> <span class="n">NativeLibrary</span><span class="p">.</span><span class="n">Load</span><span class="p">(</span><span class="s">"./foo.dll"</span><span class="p">);</span>
<span class="kt">var</span> <span class="n">foo</span> <span class="p">=</span> <span class="p">(</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">,</span> <span class="n">SuppressGCTransition</span><span class="p">]<</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">]<</span><span class="kt">int</span><span class="p">,</span> <span class="n">nint</span><span class="p">>,</span> <span class="kt">int</span><span class="p">,</span> <span class="kt">string</span><span class="p">>)</span><span class="n">NativeLibrary</span><span class="p">.</span><span class="n">GetExport</span><span class="p">(</span><span class="n">library</span><span class="p">,</span> <span class="s">"foo"</span><span class="p">);</span>
<span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">foo</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="m">5</span><span class="p">);</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">result</span><span class="p">);</span> <span class="c1">// wwwww</span>
<span class="n">NativeLibrary</span><span class="p">.</span><span class="n">Free</span><span class="p">(</span><span class="n">library</span><span class="p">);</span>
</span></code></pre></div><p>上面这些都不是 Windows 专用，在 Linux、macOS 上导入 <code>.so</code> 和 <code>.dylib</code> 都完全不在话下。</p><p><br></p><p>再有，我们有一些数据想要进行计算，但是我们想使用 SIMD 进行处理，那只需要这么写：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">vec1</span> <span class="p">=</span> <span class="n">Vector128</span><span class="p">.</span><span class="n">Create</span><span class="p">(</span><span class="m">1.1f</span><span class="p">,</span> <span class="m">2.2f</span><span class="p">,</span> <span class="m">3.3f</span><span class="p">,</span> <span class="m">4.4f</span><span class="p">);</span>
<span class="kt">var</span> <span class="n">vec2</span> <span class="p">=</span> <span class="n">Vector128</span><span class="p">.</span><span class="n">Create</span><span class="p">(</span><span class="m">5.5f</span><span class="p">,</span> <span class="m">6.6f</span><span class="p">,</span> <span class="m">7.7f</span><span class="p">,</span> <span class="m">8.8f</span><span class="p">);</span>

<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">Calc</span><span class="p">(</span><span class="n">vec1</span><span class="p">,</span> <span class="n">vec2</span><span class="p">));</span>

<span class="kt">float</span> <span class="nf">Calc</span><span class="p">(</span><span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">></span> <span class="n">l</span><span class="p">,</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">></span> <span class="n">r</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">Avx2</span><span class="p">.</span><span class="n">IsSupported</span><span class="p">)</span>
    <span class="p">&#123;</span>
        <span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">Avx2</span><span class="p">.</span><span class="n">Multiply</span><span class="p">(</span><span class="n">vec1</span><span class="p">,</span> <span class="n">vec2</span><span class="p">);</span>
        <span class="kt">float</span> <span class="n">sum</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">var</span> <span class="n">i</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span> <span class="n">i</span> <span class="p"><</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">>.</span><span class="n">Count</span><span class="p">;</span> <span class="n">i</span><span class="p">++)</span> <span class="n">sum</span> <span class="p">+=</span> <span class="n">result</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">);</span>
        <span class="k">return</span> <span class="n">sum</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="k">else</span> <span class="nf">if</span> <span class="p">(</span><span class="n">Rdm</span><span class="p">.</span><span class="n">IsSupported</span><span class="p">)</span>
    <span class="p">&#123;</span>
        <span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">Rdm</span><span class="p">.</span><span class="n">Multiply</span><span class="p">(</span><span class="n">vec1</span><span class="p">,</span> <span class="n">vec2</span><span class="p">);</span>
        <span class="kt">float</span> <span class="n">sum</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">var</span> <span class="n">i</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span> <span class="n">i</span> <span class="p"><</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">>.</span><span class="n">Count</span><span class="p">;</span> <span class="n">i</span><span class="p">++)</span> <span class="n">sum</span> <span class="p">+=</span> <span class="n">result</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">);</span>
        <span class="k">return</span> <span class="n">sum</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="k">else</span>
    <span class="p">&#123;</span>
        <span class="kt">float</span> <span class="n">sum</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span> <span class="n">i</span> <span class="p"><</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">>.</span><span class="n">Count</span><span class="p">;</span> <span class="n">i</span><span class="p">++)</span>
        <span class="p">&#123;</span>
            <span class="n">sum</span> <span class="p">+=</span> <span class="n">l</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="p">*</span> <span class="n">r</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">);</span>
        <span class="p">&#125;</span>
        <span class="k">return</span> <span class="n">sum</span><span class="p">;</span>
    <span class="p">&#125;</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>可以看看在 X86 平台上生成了什么代码：</p><div class="highlight"><pre><code class="language-text"><span>vzeroupper
vmovupdxmm0, [r8]
vmulpsxmm0, xmm0, [r8+0x10]
vmovapsxmm1, xmm0
vxorpsxmm2, xmm2, xmm2
vaddssxmm1, xmm1, xmm2
vmovshdupxmm2, xmm0
vaddssxmm1, xmm2, xmm1
vunpckhpsxmm2, xmm0, xmm0
vaddssxmm1, xmm2, xmm1
vshufpsxmm0, xmm0, xmm0, 0xff
vaddssxmm1, xmm0, xmm1
vmovapsxmm0, xmm1
ret
</span></code></pre></div><p>但其实除了手动编写 SIMD 代码之外，前两个分支完全可以不写，而只留下：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">float</span> <span class="nf">Calc</span><span class="p">(</span><span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">></span> <span class="n">l</span><span class="p">,</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">></span> <span class="n">r</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">float</span> <span class="n">sum</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="p">=</span> <span class="m">0</span><span class="p">;</span> <span class="n">i</span> <span class="p"><</span> <span class="n">Vector128</span><span class="p"><</span><span class="kt">float</span><span class="p">>.</span><span class="n">Count</span><span class="p">;</span> <span class="n">i</span><span class="p">++)</span>
    <span class="p">&#123;</span>
        <span class="n">sum</span> <span class="p">+=</span> <span class="n">l</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="p">*</span> <span class="n">r</span><span class="p">.</span><span class="n">GetElement</span><span class="p">(</span><span class="n">i</span><span class="p">);</span>
    <span class="p">&#125;</span>
    <span class="k">return</span> <span class="n">sum</span><span class="p">;</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>因为现阶段当循环边界条件是向量长度时，.NET 会自动为我们做向量化。</p><p><br></p><p>那么继续，我们还有<code>ref</code>、<code>in</code>、<code>out</code>来做引用传递。</p><p>假设我们有一个很大的 <code>struct</code>，我们为了避免传递时发生拷贝，可以直接用 <code>in</code> 来做只读引用传递：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="k">void</span> <span class="nf">Test</span><span class="p">(</span><span class="k">in</span> <span class="n">Foo</span> <span class="n">v</span><span class="p">)</span> <span class="p">&#123;</span> <span class="p">&#125;</span>

<span class="k">struct</span> <span class="nc">Foo</span>
<span class="p">&#123;</span>
    <span class="k">public</span> <span class="kt">long</span> <span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">,</span> <span class="n">C</span><span class="p">,</span> <span class="n">D</span><span class="p">,</span> <span class="n">E</span><span class="p">,</span> <span class="n">F</span><span class="p">,</span> <span class="n">G</span><span class="p">,</span> <span class="n">H</span><span class="p">,</span> <span class="n">I</span><span class="p">,</span> <span class="n">J</span><span class="p">,</span> <span class="n">K</span><span class="p">,</span> <span class="n">L</span><span class="p">,</span> <span class="n">M</span><span class="p">,</span> <span class="n">N</span><span class="p">;</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>而对于小的 <code>struct</code>，.NET 有专门的优化帮我们彻底消除掉内存分配，完全将 <code>struct</code> 放在寄存器中，例如如下代码：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">double</span> <span class="nf">Test</span><span class="p">(</span><span class="kt">int</span> <span class="n">x1</span><span class="p">,</span> <span class="kt">int</span> <span class="n">y1</span><span class="p">,</span> <span class="kt">int</span> <span class="n">x2</span><span class="p">,</span> <span class="kt">int</span> <span class="n">y2</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">p1</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">y1</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">p2</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p">(</span><span class="n">x2</span><span class="p">,</span> <span class="n">y2</span><span class="p">);</span>
    <span class="k">return</span> <span class="nf">GetDistance</span><span class="p">(</span><span class="n">p1</span><span class="p">,</span> <span class="n">p2</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="na">[MethodImpl(MethodImplOptions.AggressiveInlining)]</span>
<span class="kt">double</span> <span class="nf">GetDistance</span><span class="p">(</span><span class="n">Point</span> <span class="n">a</span><span class="p">,</span> <span class="n">Point</span> <span class="n">b</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="k">return</span> <span class="n">Math</span><span class="p">.</span><span class="n">Sqrt</span><span class="p">((</span><span class="n">a</span><span class="p">.</span><span class="n">X</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">X</span><span class="p">)</span> <span class="p">*</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">X</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">X</span><span class="p">)</span> <span class="p">+</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">Y</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">Y</span><span class="p">)</span> <span class="p">*</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">Y</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">Y</span><span class="p">));</span>
<span class="p">&#125;</span>

<span class="k">struct</span> <span class="nc">Point</span>
<span class="p">&#123;</span>
    <span class="k">public</span> <span class="nf">Point</span><span class="p">(</span><span class="kt">int</span> <span class="n">x</span><span class="p">,</span> <span class="kt">int</span> <span class="n">y</span><span class="p">)</span>
    <span class="p">&#123;</span>
        <span class="n">X</span> <span class="p">=</span> <span class="n">x</span><span class="p">;</span> <span class="n">Y</span> <span class="p">=</span> <span class="n">y</span><span class="p">;</span>
    <span class="p">&#125;</span>
    
    <span class="k">public</span> <span class="kt">int</span> <span class="n">X</span> <span class="p">&#123;</span> <span class="k">get</span><span class="p">;</span> <span class="k">set</span><span class="p">;</span> <span class="p">&#125;</span>
    <span class="k">public</span> <span class="kt">int</span> <span class="n">Y</span> <span class="p">&#123;</span> <span class="k">get</span><span class="p">;</span> <span class="k">set</span><span class="p">;</span> <span class="p">&#125;</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>上述代码 <code>GetDistance</code> 考虑是个热点路径，因此我加 <code>MethodImplOptions.AggressiveInlining</code> 来指导 JIT 有保证地内联此函数，最后为 <code>Test</code> 生成了如下的代码：</p><div class="highlight"><pre><code class="language-text"><span>vzeroupper
subecx, r8d
moveax, ecx
imuleax, ecx
subedx, r9d
movecx, edx
imuledx, ecx
addeax, edx
vxorpsxmm0, xmm0, xmm0
vcvtsi2sdxmm0, xmm0, eax
vsqrtsdxmm0, xmm0, xmm0
ret
</span></code></pre></div><p>全程没有一句指令访存，非常的高效。</p><p>我们还可以借用 <code>ref</code> 的引用语义来做原地更新： </p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">vec</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Vector</span><span class="p">(</span><span class="m">10</span><span class="p">);</span>
<span class="n">vec</span><span class="p">[</span><span class="m">2</span><span class="p">]</span> <span class="p">=</span> <span class="m">5</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">vec</span><span class="p">[</span><span class="m">2</span><span class="p">]);</span> <span class="c1">// 5</span>
<span class="k">ref</span> <span class="kt">var</span> <span class="n">x</span> <span class="p">=</span> <span class="k">ref</span> <span class="n">vec</span><span class="p">[</span><span class="m">3</span><span class="p">];</span>
<span class="n">x</span> <span class="p">=</span> <span class="m">7</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">vec</span><span class="p">[</span><span class="m">3</span><span class="p">]);</span> <span class="c1">// 7</span>

<span class="k">class</span> <span class="nc">Vector</span>
<span class="p">&#123;</span>
    <span class="k">private</span> <span class="kt">int</span><span class="p">[]</span> <span class="n">_array</span><span class="p">;</span>
    <span class="k">public</span> <span class="nf">Vector</span><span class="p">(</span><span class="kt">int</span> <span class="n">count</span><span class="p">)</span> <span class="p">=></span> <span class="n">_array</span> <span class="p">=</span> <span class="k">new</span> <span class="kt">int</span><span class="p">[</span><span class="n">count</span><span class="p">];</span>
    <span class="k">public</span> <span class="k">ref</span> <span class="kt">int</span> <span class="k">this</span><span class="p">[</span><span class="kt">int</span> <span class="n">index</span><span class="p">]</span> <span class="p">=></span> <span class="k">ref</span> <span class="n">_array</span><span class="p">[</span><span class="n">index</span><span class="p">];</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>甚至还能搭配指针和手动分配内存来使用：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">vec</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Vector</span><span class="p">(</span><span class="m">10</span><span class="p">);</span>
<span class="n">vec</span><span class="p">[</span><span class="m">2</span><span class="p">]</span> <span class="p">=</span> <span class="m">5</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">vec</span><span class="p">[</span><span class="m">2</span><span class="p">]);</span> <span class="c1">// 5</span>
<span class="k">ref</span> <span class="kt">var</span> <span class="n">x</span> <span class="p">=</span> <span class="k">ref</span> <span class="n">vec</span><span class="p">[</span><span class="m">3</span><span class="p">];</span>
<span class="n">x</span> <span class="p">=</span> <span class="m">7</span><span class="p">;</span>
<span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">vec</span><span class="p">[</span><span class="m">3</span><span class="p">]);</span> <span class="c1">// 7</span>

<span class="k">unsafe</span> <span class="k">class</span> <span class="nc">Vector</span>
<span class="p">&#123;</span>
    <span class="k">private</span> <span class="kt">int</span><span class="p">*</span> <span class="n">_memory</span><span class="p">;</span>
    <span class="k">public</span> <span class="nf">Vector</span><span class="p">(</span><span class="kt">uint</span> <span class="n">count</span><span class="p">)</span> <span class="p">=></span> <span class="n">_memory</span> <span class="p">=</span> <span class="p">(</span><span class="kt">int</span><span class="p">*)</span><span class="n">NativeMemory</span><span class="p">.</span><span class="n">Alloc</span><span class="p">(</span><span class="n">count</span><span class="p">,</span> <span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>
    <span class="k">public</span> <span class="k">ref</span> <span class="kt">int</span> <span class="k">this</span><span class="p">[</span><span class="kt">int</span> <span class="n">index</span><span class="p">]</span> <span class="p">=></span> <span class="k">ref</span> <span class="n">_memory</span><span class="p">[</span><span class="n">index</span><span class="p">];</span>
    <span class="p">~</span><span class="n">Vector</span><span class="p">()</span> <span class="p">=></span> <span class="n">NativeMemory</span><span class="p">.</span><span class="n">Free</span><span class="p">(</span><span class="n">_memory</span><span class="p">);</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>C# 的泛型不像 Java 采用擦除，而是真真正正会对所有的类型参数特化代码（尽管对于引用类型会共享实现采用运行时分发），这也就意味着能最大程度确保性能，并且对应的类型拥有根据类型参数大小不同而特化的内存布局。还是上面那个 <code>Point</code> 的例子，我们将下面的数据 <code>int</code> 换成泛型参数 <code>T</code>，并做值类型数字的泛型约束：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">double</span> <span class="nf">Test1</span><span class="p">(</span><span class="kt">double</span> <span class="n">x1</span><span class="p">,</span> <span class="kt">double</span> <span class="n">y1</span><span class="p">,</span> <span class="kt">double</span> <span class="n">x2</span><span class="p">,</span> <span class="kt">double</span> <span class="n">y2</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">p1</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p"><</span><span class="kt">double</span><span class="p">>(</span><span class="n">x1</span><span class="p">,</span> <span class="n">y1</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">p2</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p"><</span><span class="kt">double</span><span class="p">>(</span><span class="n">x2</span><span class="p">,</span> <span class="n">y2</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">GetDistanceSquare</span><span class="p">(</span><span class="n">p1</span><span class="p">,</span> <span class="n">p2</span><span class="p">);</span>
    <span class="k">return</span> <span class="n">Math</span><span class="p">.</span><span class="n">Sqrt</span><span class="p">(</span><span class="n">result</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="kt">double</span> <span class="nf">Test2</span><span class="p">(</span><span class="kt">int</span> <span class="n">x1</span><span class="p">,</span> <span class="kt">int</span> <span class="n">y1</span><span class="p">,</span> <span class="kt">int</span> <span class="n">x2</span><span class="p">,</span> <span class="kt">int</span> <span class="n">y2</span><span class="p">)</span>
<span class="p">&#123;</span>
    <span class="kt">var</span> <span class="n">p1</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p"><</span><span class="kt">int</span><span class="p">>(</span><span class="n">x1</span><span class="p">,</span> <span class="n">y1</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">p2</span> <span class="p">=</span> <span class="k">new</span> <span class="n">Point</span><span class="p"><</span><span class="kt">int</span><span class="p">>(</span><span class="n">x2</span><span class="p">,</span> <span class="n">y2</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">result</span> <span class="p">=</span> <span class="n">GetDistanceSquare</span><span class="p">(</span><span class="n">p1</span><span class="p">,</span> <span class="n">p2</span><span class="p">);</span>
    <span class="k">return</span> <span class="n">Math</span><span class="p">.</span><span class="n">Sqrt</span><span class="p">(</span><span class="n">result</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="na">[MethodImpl(MethodImplOptions.AggressiveInlining)]</span>
<span class="n">T</span> <span class="n">GetDistanceSquare</span><span class="p"><</span><span class="n">T</span><span class="p">>(</span><span class="n">Point</span><span class="p"><</span><span class="n">T</span><span class="p">></span> <span class="n">a</span><span class="p">,</span> <span class="n">Point</span><span class="p"><</span><span class="n">T</span><span class="p">></span> <span class="n">b</span><span class="p">)</span> <span class="k">where</span> <span class="n">T</span> <span class="p">:</span> <span class="n">struct</span><span class="p">,</span> <span class="n">IBinaryNumber</span><span class="p"><</span><span class="n">T</span><span class="p">></span>
<span class="p">&#123;</span>
    <span class="k">return</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">X</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">X</span><span class="p">)</span> <span class="p">*</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">X</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">X</span><span class="p">)</span> <span class="p">+</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">Y</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">Y</span><span class="p">)</span> <span class="p">*</span> <span class="p">(</span><span class="n">a</span><span class="p">.</span><span class="n">Y</span> <span class="p">-</span> <span class="n">b</span><span class="p">.</span><span class="n">Y</span><span class="p">);</span>
<span class="p">&#125;</span>

<span class="k">struct</span> <span class="nc">Point</span><span class="p"><</span><span class="n">T</span><span class="p">></span> <span class="k">where</span> <span class="n">T</span> <span class="p">:</span> <span class="n">struct</span><span class="p">,</span> <span class="n">IBinaryNumber</span><span class="p"><</span><span class="n">T</span><span class="p">></span>
<span class="p">&#123;</span>
    <span class="k">public</span> <span class="nf">Point</span><span class="p">(</span><span class="n">T</span> <span class="n">x</span><span class="p">,</span> <span class="n">T</span> <span class="n">y</span><span class="p">)</span>
    <span class="p">&#123;</span>
        <span class="n">X</span> <span class="p">=</span> <span class="n">x</span><span class="p">;</span> <span class="n">Y</span> <span class="p">=</span> <span class="n">y</span><span class="p">;</span>
    <span class="p">&#125;</span>

    <span class="k">public</span> <span class="n">T</span> <span class="n">X</span> <span class="p">&#123;</span> <span class="k">get</span><span class="p">;</span> <span class="k">set</span><span class="p">;</span> <span class="p">&#125;</span>
    <span class="k">public</span> <span class="n">T</span> <span class="n">Y</span> <span class="p">&#123;</span> <span class="k">get</span><span class="p">;</span> <span class="k">set</span><span class="p">;</span> <span class="p">&#125;</span>
<span class="p">&#125;</span>
</span></code></pre></div><p>无论是 <code>Test1</code> 还是 <code>Test2</code>，生成的代码都非常优秀，不仅不存在任何的装箱拆箱，甚至没有任何的访存操作：</p><div class="highlight"><pre><code class="language-text"><span>' Test1
vzeroupper
vsubsdxmm0, xmm0, xmm2
vmovapsxmm2, xmm0
vmulsdxmm0, xmm0, xmm2
vsubsdxmm1, xmm1, xmm3
vmovapsxmm2, xmm1
vmulsdxmm1, xmm1, xmm2
vaddsdxmm0, xmm1, xmm0
vsqrtsdxmm0, xmm0, xmm0
ret

' Test2
vzeroupper
subecx, r8d
moveax, ecx
imuleax, ecx
subedx, r9d
movecx, edx
imuledx, ecx
addeax, edx
vxorpsxmm0, xmm0, xmm0
vcvtsi2sdxmm0, xmm0, eax
vsqrtsdxmm0, xmm0, xmm0
ret
</span></code></pre></div><p><br></p><p>接着讲，我们有时候为了高性能想要临时暂停 GC 的回收，只需要简单的一句：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="n">GC</span><span class="p">.</span><span class="n">TryStartNoGCRegion</span><span class="p">(</span><span class="m">1024</span> <span class="p">*</span> <span class="m">1024</span> <span class="p">*</span> <span class="m">128</span><span class="p">);</span>
</span></code></pre></div><p>就能告诉 GC 如果还能分配 128mb 内存那就不要做回收了，然后一段时间内以后的代码我们尽管在这个预算内分配内存，任何 GC 都不会发生。甚至还能阻止在内存不够分配的情况下进行阻塞式 Full GC：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="n">GC</span><span class="p">.</span><span class="n">TryStartNoGCRegion</span><span class="p">(</span><span class="m">1024</span> <span class="p">*</span> <span class="m">1024</span> <span class="p">*</span> <span class="m">128</span><span class="p">,</span> <span class="k">true</span><span class="p">);</span>
</span></code></pre></div><p>代码执行完了，最后的时候调用一句：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="n">GC</span><span class="p">.</span><span class="n">EndNoGCRegion</span><span class="p">();</span>
</span></code></pre></div><p>即可恢复 GC 行为。</p><p>除此之外，我们还能在运行时指定 GC 的模式来最大化性能：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="n">GCSettings</span><span class="p">.</span><span class="n">LatencyMode</span> <span class="p">=</span> <span class="n">GCLatencyMode</span><span class="p">.</span><span class="n">Batch</span><span class="p">;</span>
<span class="n">GCSettings</span><span class="p">.</span><span class="n">LatencyMode</span> <span class="p">=</span> <span class="n">GCLatencyMode</span><span class="p">.</span><span class="n">Interactive</span><span class="p">;</span>
<span class="n">GCSettings</span><span class="p">.</span><span class="n">LatencyMode</span> <span class="p">=</span> <span class="n">GCLatencyMode</span><span class="p">.</span><span class="n">LowLatency</span><span class="p">;</span>
<span class="n">GCSettings</span><span class="p">.</span><span class="n">LatencyMode</span> <span class="p">=</span> <span class="n">GCLatencyMode</span><span class="p">.</span><span class="n">NoGCRegion</span><span class="p">;</span>
<span class="n">GCSettings</span><span class="p">.</span><span class="n">LatencyMode</span> <span class="p">=</span> <span class="n">GCLatencyMode</span><span class="p">.</span><span class="n">SustainedLowLatency</span><span class="p">;</span>
</span></code></pre></div><p><br></p><p>更进一步，我们甚至可以直接将堆内存中的代码执行，在 .NET 上自己造一个 JIT，直接从内存创建一块可执行的区域然后往里面塞一段代码用来将两个32位整数相加：</p><div class="highlight"><pre><code class="language-csharp"><span><span class="kt">var</span> <span class="n">kernel32</span> <span class="p">=</span> <span class="n">NativeLibrary</span><span class="p">.</span><span class="n">Load</span><span class="p">(</span><span class="s">"kernel32.dll"</span><span class="p">);</span>
<span class="kt">var</span> <span class="n">virtualProtectEx</span> <span class="p">=</span> <span class="p">(</span><span class="k">delegate</span><span class="p">*</span> <span class="n">unmanaged</span><span class="p">[</span><span class="n">Cdecl</span><span class="p">,</span> <span class="n">SuppressGCTransition</span><span class="p">]<</span><span class="n">nint</span><span class="p">,</span> <span class="k">void</span><span class="p">*,</span> <span class="n">nint</span><span class="p">,</span> <span class="kt">int</span><span class="p">,</span> <span class="k">out</span> <span class="kt">int</span><span class="p">,</span> <span class="kt">bool</span><span class="p">>)</span><span class="n">NativeLibrary</span><span class="p">.</span><span class="n">GetExport</span><span class="p">(</span><span class="n">kernel32</span><span class="p">,</span> <span class="s">"VirtualProtectEx"</span><span class="p">);</span>
<span class="kt">var</span> <span class="n">processHandle</span> <span class="p">=</span> <span class="n">Process</span><span class="p">.</span><span class="n">GetCurrentProcess</span><span class="p">().</span><span class="n">Handle</span><span class="p">;</span>

<span class="n">Memory</span><span class="p"><</span><span class="kt">byte</span><span class="p">></span> <span class="n">code</span> <span class="p">=</span> <span class="k">new</span> <span class="kt">byte</span><span class="p">[]</span> <span class="p">&#123;</span>
    <span class="m">0</span><span class="n">x8d</span><span class="p">,</span> <span class="m">0</span><span class="n">x04</span><span class="p">,</span> <span class="m">0</span><span class="n">x11</span><span class="p">,</span> <span class="c1">// lea rax, [rcx+rdx]</span>
    <span class="m">0</span><span class="n">xc3</span>              <span class="c1">// ret</span>
<span class="p">&#125;</span>

<span class="k">using</span> <span class="p">(</span><span class="kt">var</span> <span class="n">handle</span> <span class="p">=</span> <span class="n">code</span><span class="p">.</span><span class="n">Pin</span><span class="p">())</span>
<span class="p">&#123;</span>
    <span class="n">virtualProtectEx</span><span class="p">(</span><span class="n">processHandle</span><span class="p">,</span> <span class="n">handle</span><span class="p">.</span><span class="n">Pointer</span><span class="p">,</span> <span class="n">code</span><span class="p">.</span><span class="n">Length</span><span class="p">,</span> <span class="m">0</span><span class="n">x40</span><span class="p">,</span> <span class="k">out</span> <span class="n">_</span><span class="p">);</span>
    <span class="kt">var</span> <span class="n">f</span> <span class="p">=</span> <span class="p">(</span><span class="k">delegate</span><span class="p">*<</span><span class="kt">int</span><span class="p">,</span> <span class="kt">int</span><span class="p">,</span> <span class="kt">int</span><span class="p">>)</span><span class="n">handle</span><span class="p">.</span><span class="n">Pointer</span><span class="p">;</span>
    <span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">f</span><span class="p">(</span><span class="m">2</span><span class="p">,</span> <span class="m">3</span><span class="p">));</span> <span class="c1">// 5</span>
<span class="p">&#125;</span>

<span class="n">virtualProtectEx</span> <span class="p">=</span> <span class="k">null</span><span class="p">;</span>
<span class="n">NativeLibrary</span><span class="p">.</span><span class="n">Free</span><span class="p">(</span><span class="n">kernel32</span><span class="p">);</span>
</span></code></pre></div><p><br></p><p>除此之外，C# 还有更多数不清的底层写法来和操作系统交互，甚至利用 C# 的编译器取消链接到自己的标准库，直接用从 0 开始造基础类型然后通过 NativeAOT 编译出完全无 GC、能够在裸机硬件上执行引导系统的 EFI 固件都是没有问题的，参考 <a href="http://link.zhihu.com/?target=https%3A//github.com/MichalStrehovsky/zerosharp" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/MichalStreho</span><span class="invisible">vsky/zerosharp</span><span class="ellipsis"></span></a></p><p><br></p><p>另外还有 ILGPU 让你把 C# 代码直接跑在 GPU 上面，以及跑在嵌入式设备上直接操作 I2C、PWM、GPIO 等等，就不再举例子了。</p><p><br></p><p>而 C# 已经进了 roadmap 的后续更新内容：允许声明引用字段、添加表达固定长度内存的类型、允许传数组时消除数组分配、允许在栈上分配任何对象等等，无一不是在改进这些底层性能设施。</p><p><br></p><p>以上就是我认为的 C# 和 Java 最大的不同。</p><p>在 C# 中当你不需要上面这些的东西时，它们仿佛从来都不存在，允许动态类型、不断吸收各种函数式特性、还有各种语法糖加持，简洁度和灵活度甚至不输 Python，非常愉快和简单地就能编写各种代码；而一旦你需要，你可以拥有从上层到底层的几乎完全的控制能力，而这些能力将能让你有需要时无需思考各种奇怪的 workaround 就能直接榨干机器，达到 C、C++ 的性能，甚至因为有运行时 PGO 而超出 C、C++ 的性能。</p>  
</div>
            