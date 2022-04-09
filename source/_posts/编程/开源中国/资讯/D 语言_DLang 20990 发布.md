
---
title: 'D 语言_DLang 2.099.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4040'
author: 开源中国
comments: false
date: Sat, 09 Apr 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4040'
---

<div>   
<div class="content">
                                                                    
                                                        <p>D 语言/DLang 2.099.0 已于上月发布。</p> 
<p>公告显示，这是一个重大版本，更新亮点包括：</p> 
<ul> 
 <li>D 代码模块可通过 ImportC 被导入 C 代码中</li> 
 <li>引入抛出表达式 (throw expression)</li> 
 <li>PE/COFF 输出现在是 DMD 在 Windows 上的默认输出</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.099.0.html" target="_blank">详情查看 Changelog</a>。</p> 
<p><strong>使用 ImportC 在 C 源码中导入 D 代码模块</strong></p> 
<p>从 D 2.099.0 开始，可通过<code>__import</code>关键字直接将 D 代码模块导入 C 文件。</p> 
<pre><code>// dsayhello.d
import core.stdc.stdio : puts;

extern(C) void helloImport() &#123;
    puts("Hello __import!");
&#125;</code></pre> 
<pre><code>// dhelloimport.c
__import dsayhello;
__import core.stdc.stdio : puts;

int main(int argc, char** argv) &#123;
    helloImport();
    puts("Cool, eh?");
    return 0;
&#125;</code></pre> 
<p>使用如下代码进行编译：</p> 
<pre><code>dmd dhelloimport.c dsayhello.d</code></pre> 
<p>此外还可导入已经通过 ImportC 编译过的 C 代码模块：</p> 
<pre><code>// csayhello.c
__import core.stdc.stdio : puts;

void helloImport() &#123;
    puts("Hello _import!");
&#125;</code></pre> 
<pre><code>// chelloimport.c
__import csayhello;
__import core.stdc.stdio : puts;

int main(int argc, char** argv) &#123;
    helloImport();
    puts("Cool, eh?");
    return 0;
&#125;</code></pre> 
<p>使用如下代码进行编译：</p> 
<pre><code>dmd chelloimport.c csayhello.c</code></pre> 
<p><strong>引入抛出表达式 (throw expression)</strong></p> 
<p>在 D 语言的生命周期中，<code>throw</code>属于声明(statement )，不能在表达式中使用，因为表达式必须有一个类型，而由于<code>throw</code>不返回值，所以没有合适的类型，这导致它不能使用以下语法。</p> 
<pre><code>(string err) => throw new Exception(err);</code></pre> 
<p>只能使用如下的方案：</p> 
<pre><code>(string err) &#123; throw new Exception(err); &#125;</code></pre> 
<p>不过从 D 2.099.0 开始，以下代码片段可通过编译：</p> 
<pre><code>void foo(int function() f) &#123;&#125;

void main() &#123;
    foo(() => throw new Exception());
&#125;</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.099.1.html" target="_blank">详情查看 Changelog</a>。</p> 
<hr> 
<p>P.S. 发稿前看到最新版本为<strong style="color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdownloads.dlang.org%2Freleases%2F2.x%2F2.099.1" target="_blank"> 2.099.1</a></strong>。更新内容主要是修复错误，以及两项关于编译器和库的重要变更。</p>
                                        </div>
                                      
</div>
            