
---
title: '最简单的 UE 4 C++ 教程 ——触发改变网格的材质【三十】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6990795055917170725'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 11:23:55 GMT
thumbnail: 'https://juejin.cn/post/6990795055917170725'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p>\</p>
<p><strong>原教程是基于 UE 4.18，我是基于 UE 4.25】</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Fchange-material-mesh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unrealcpp.com/change-material-mesh/" ref="nofollow noopener noreferrer">英文原地址</a></p>
<p>在本教程中，当发生重叠事件时，我们将改变静态网格的材质。首先，创建一个新的 Actor 子类，在本教程中我叫它 <strong>ChangeMaterialMesh</strong>。</p>
<p>首先，在 .h 文件中，我们将创建一个 <strong>UStaticMeshComponent</strong> 、两个 <strong>UMaterial</strong> 类和一个<strong>UBoxComponent</strong>。将元素添加到头文件的公共部分。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">...
<span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UStaticMeshComponent</span>* <span class="hljs-title">MyMesh</span>;</span>

<span class="hljs-built_in">UPROPERTY</span>(EditAnywhere)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UMaterial</span>* <span class="hljs-title">OnMaterial</span>;</span>

<span class="hljs-built_in">UPROPERTY</span>(EditAnywhere)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UMaterial</span>* <span class="hljs-title">OffMaterial</span>;</span>

<span class="hljs-built_in">UPROPERTY</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UBoxComponent</span>* <span class="hljs-title">MyBoxComponent</span>;</span>

<span class="hljs-built_in">UFUNCTION</span>()
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">OnOverlapBegin</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, <span class="hljs-keyword">bool</span> bFromSweep, <span class="hljs-keyword">const</span> FHitResult& SweepResult)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们进入 .cpp 文件。首先，在顶部包含 <strong><code>DrawDebugHelpers.h</code></strong> 和<strong>Components/BoxComponent.h</strong> 文件，这样我们就可以可视化和使用我们的碰撞框。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// include draw debug helpers header file</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"DrawDebugHelpers.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Components/BoxComponent.h"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，我们将设置构造函数并设置默认值。使用 <strong>CreateDefaultSubobject</strong> 创建静态网格，并将其设置为 <strong>RootComponent</strong> 。然后，通过 <strong>CreateDefaultSubobject</strong> 创建盒子组件，我们将通过使用 <strong>InitBoxExtent</strong> 将它的大小范围设置为 <strong>FVector(100,100,100)</strong> 。盒子组件将初始化为一个名为 <strong>Trigger</strong> 的碰撞配置文件，并将被附加到 <strong>RootComponent</strong> 上。接下来，创建两个材质的网格之间切换，建立 bool 的默认值，最后连接重叠函数。</p>
<p>下面是构造函数代码。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">AChangeMaterialMesh::<span class="hljs-built_in">AChangeMaterialMesh</span>()
&#123;
 <span class="hljs-comment">// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.</span>
PrimaryActorTick.bCanEverTick = <span class="hljs-literal">true</span>;

MyMesh = CreateDefaultSubobject<UStaticMeshComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"MyMesh"</span>));
RootComponent = MyMesh;

MyBoxComponent = CreateDefaultSubobject<UBoxComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"MyBoxComponent"</span>));
MyBoxComponent-><span class="hljs-built_in">InitBoxExtent</span>(<span class="hljs-built_in">FVector</span>(<span class="hljs-number">100</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>));
MyBoxComponent-><span class="hljs-built_in">SetCollisionProfileName</span>(<span class="hljs-string">"Trigger"</span>);
MyBoxComponent-><span class="hljs-built_in">SetupAttachment</span>(RootComponent);

OnMaterial = CreateDefaultSubobject<UMaterial>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"OnMaterial"</span>));
OffMaterial = CreateDefaultSubobject<UMaterial>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"OffMaterial"</span>));

MyBoxComponent->OnComponentBeginOverlap.<span class="hljs-built_in">AddDynamic</span>(<span class="hljs-keyword">this</span>, &AChangeMaterialMesh::OnOverlapBegin);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，在 <strong>BeginPlay()</strong> 方法中，我们将使用 <strong>DrawDebugBox</strong> 绘制调试框，并使用 <strong>SetMaterial</strong> 设置网格的第一个材质。下面是 <strong>BeginPlay()</strong> 代码。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AChangeMaterialMesh::BeginPlay</span><span class="hljs-params">()</span>
</span>&#123;
Super::<span class="hljs-built_in">BeginPlay</span>();

<span class="hljs-built_in">DrawDebugBox</span>(<span class="hljs-built_in">GetWorld</span>(), <span class="hljs-built_in">GetActorLocation</span>(), <span class="hljs-built_in">FVector</span>(<span class="hljs-number">100</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>), FColor::White, <span class="hljs-literal">true</span>, <span class="hljs-number">-1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">10</span>);

MyMesh-><span class="hljs-built_in">SetMaterial</span>(<span class="hljs-number">0</span>, OffMaterial);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，我们将创建一个重叠函数来改变网格的材质。我们将检查 <strong>OtherActor</strong> 是否不为空，<strong>OtherActor</strong> 是否不是同一个 actor，以及 <strong>OtherComp</strong> 是否不为空。如果一切都通过了，我们将调用 <strong>SetMaterial</strong> 并传入新的材质，并将其设置为网格的第一个材质。</p>
<p>下面是重叠函数。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AChangeMaterialMesh::OnOverlapBegin</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, <span class="hljs-keyword">bool</span> bFromSweep, <span class="hljs-keyword">const</span> FHitResult& SweepResult)</span> 
</span>&#123;
<span class="hljs-keyword">if</span> ( (OtherActor != <span class="hljs-literal">nullptr</span> ) && (OtherActor != <span class="hljs-keyword">this</span>) && ( OtherComp != <span class="hljs-literal">nullptr</span> ) ) 
&#123;
MyMesh-><span class="hljs-built_in">SetMaterial</span>(<span class="hljs-number">0</span>, OnMaterial);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译代码。将 actor 拖放到游戏世界中。在细节面板中添加一个网格，并向 actor 添加两个材质(这些材质是在父组件 (实例) 的细节面板中设置的)。现在当你按下播放时，网格将在发生重叠时改变材质。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13133aa425b1457d8a777f1fe4c53cb0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f26824a16ab424dad58bd2e406bf776~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/694e0759adc444eda2f2c7660b640b00~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990795055917170725" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>​</p></div>  
</div>
            