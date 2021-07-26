
---
title: '最简单的 UE 4 C++ 教程 —— 创建静态网格【二】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76ba39e62a6347f5a56b7bd7639d9b57~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 07:11:03 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76ba39e62a6347f5a56b7bd7639d9b57~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>【原教程是基于 UE 4.18，我是基于 UE 4.25】</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Fcreate-static-mesh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unrealcpp.com/create-static-mesh/" ref="nofollow noopener noreferrer">英文源地址</a></p>
<p>接上一节教程，创建一个新的继承自 Actor 的 C++  类并将其命名为 <strong>CreateStaticMesh</strong> 。在头文件中添加<strong>UStaticMeshComponent</strong>，然后随意命名它。在这个例子中，我将其命名为 “SuperMesh”。我们将变量的 <strong>UPROPERTY</strong> 设置为 <strong>VisibleAnywhere</strong> ，这样我们就可以轻松地在编辑器中添加一个网格，如下图所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76ba39e62a6347f5a56b7bd7639d9b57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
 </p>
<p>下面是最终的头代码</p>
<h3 data-id="heading-0"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a> CreateStaticMesh.h</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> once</span>

<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CoreMinimal.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"GameFramework/Actor.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CreateStaticMesh.generated.h"</span></span>

<span class="hljs-built_in">UCLASS</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UNREALCPP_API</span> <span class="hljs-title">ACreateStaticMesh</span> :</span> <span class="hljs-keyword">public</span> AActor
&#123;
<span class="hljs-built_in">GENERATED_BODY</span>()

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Sets default values for this actor's properties</span>
<span class="hljs-built_in">ACreateStaticMesh</span>();

<span class="hljs-keyword">protected</span>:
<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">BeginPlay</span><span class="hljs-params">()</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere)
UStaticMeshComponent* SuperMesh;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 cpp 文件中，我们在 actor 类的构造函数中添加一个简单的静态网格组件。使用 <strong>CreateDefaultSubobject</strong> 创建一个新的 <strong>UStaticMeshComponent</strong>，你可以任意为它取名。在这个例子中，我把这个网格叫做 “My Super Mesh” 。</p>
<p>下面是最终的.cpp代码。</p>
<h3 data-id="heading-1">CreateStaticMesh.cpp</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CreateStaticMesh.h"</span></span>


<span class="hljs-comment">// Sets default values</span>
ACreateStaticMesh::<span class="hljs-built_in">ACreateStaticMesh</span>()
&#123;
 <span class="hljs-comment">// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.</span>
PrimaryActorTick.bCanEverTick = <span class="hljs-literal">true</span>;

<span class="hljs-comment">// Add static mesh component to actor</span>
SuperMesh = CreateDefaultSubobject<UStaticMeshComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"My Super Mesh"</span>));

&#125;

<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ACreateStaticMesh::BeginPlay</span><span class="hljs-params">()</span>
</span>&#123;
Super::<span class="hljs-built_in">BeginPlay</span>();

&#125;

<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ACreateStaticMesh::Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span>
</span>&#123;
Super::<span class="hljs-built_in">Tick</span>(DeltaTime);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在在编辑器中，拖放您的新 actor。在 actor 的Details面板中，选择你想要添加到 actor 的静态网格。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15da36dbae0a46d7bb70768e02b2ffbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            