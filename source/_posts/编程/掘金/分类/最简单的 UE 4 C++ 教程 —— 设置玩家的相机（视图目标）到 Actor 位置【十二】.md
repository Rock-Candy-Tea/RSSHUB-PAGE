
---
title: '最简单的 UE 4 C++ 教程 —— 设置玩家的相机（视图目标）到 Actor 位置【十二】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6989312701042262029'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 11:13:20 GMT
thumbnail: 'https://juejin.cn/post/6989312701042262029'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p><strong>【原教程是基于 UE 4.18，我是基于 UE 4.25】</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Fset-view-target%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unrealcpp.com/set-view-target/" ref="nofollow noopener noreferrer">英文原地址</a></p>
<p>接上一节教程，在这个简单的教程中，我们将在游戏开始时简单地改变玩家的视图目标。</p>
<p>创建一个新的 C++ Actor 子类并将其命名为 <strong>SetViewTarget</strong> 。在头文件中，我们将声明一个 actor 变量，并将其称为 <strong>MyActor</strong> 并使该 actor 在任何地方都可编辑。</p>
<h3 data-id="heading-0">SetViewTarget.h</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> once</span>

<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CoreMinimal.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"GameFramework/Actor.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"SetViewTarget.generated.h"</span></span>

<span class="hljs-built_in">UCLASS</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UNREALCPP_API</span> <span class="hljs-title">ASetViewTarget</span> :</span> <span class="hljs-keyword">public</span> AActor
&#123;
<span class="hljs-built_in">GENERATED_BODY</span>()

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Sets default values for this actor's properties</span>
<span class="hljs-built_in">ASetViewTarget</span>();

<span class="hljs-keyword">protected</span>:
<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">BeginPlay</span><span class="hljs-params">()</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-comment">// declare variables</span>
<span class="hljs-built_in">UPROPERTY</span>(EditAnywhere)
AActor* MyActor;

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989312701042262029" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，为了拥有玩家，我们需要 <strong>#include Kismet/GameplayStatics.h</strong> 文件。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"SetViewTarget.h"</span></span>
<span class="hljs-comment">// include gameplay statics header file</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Kismet/GameplayStatics.h"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989312701042262029" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这个例子中，我们所有的逻辑都放在了 <strong>BeginPlay</strong> 函数中【不是构造函数中哦，不然 UE4 可能会崩溃】。我们需要通过执行<strong>UGameplayStatics::GetPlayerController(this, 0)</strong> 来拥有当前玩家。这将获得游戏场景中的第一个玩家。接下来我们将使用 <strong>SetViewTarget(MyActor)</strong> 将我们拥有的玩家的视图目标设置为我们的<strong>MyActor</strong> 变量。</p>
<p>下面是最后的 .cpp 文件。</p>
<h3 data-id="heading-1">SetViewTarget.cpp</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"SetViewTarget.h"</span></span>
<span class="hljs-comment">// include gameplay statics header file</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Kismet/GameplayStatics.h"</span></span>


<span class="hljs-comment">// Sets default values</span>
ASetViewTarget::<span class="hljs-built_in">ASetViewTarget</span>()
&#123;
 <span class="hljs-comment">// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.</span>
PrimaryActorTick.bCanEverTick = <span class="hljs-literal">true</span>;

&#125;

<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ASetViewTarget::BeginPlay</span><span class="hljs-params">()</span>
</span>&#123;
Super::<span class="hljs-built_in">BeginPlay</span>();

<span class="hljs-comment">//Find the actor that handles control for the local player.</span>
APlayerController* OurPlayerController = UGameplayStatics::<span class="hljs-built_in">GetPlayerController</span>(<span class="hljs-keyword">this</span>, <span class="hljs-number">0</span>);

<span class="hljs-comment">//Cut instantly to our actor on begin play.</span>
OurPlayerController-><span class="hljs-built_in">SetViewTarget</span>(MyActor);

&#125;

<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ASetViewTarget::Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span>
</span>&#123;
Super::<span class="hljs-built_in">Tick</span>(DeltaTime);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989312701042262029" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译代码。将新 actor 拖放到游戏中。在编辑器中，向 actor 的细节面板中的 MyActor 变量添加一个静态网格。按下播放按钮，玩家的摄像机将会显示在新的 actor 上。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba99f3ba1094403eb872d2adfc24683c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​</p>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be36152abd2040548fb3a109f21bf678~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>第一玩家的视角</p>
<p><img src="https://juejin.cn/post/6989312701042262029" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63b3151c0f844d309ddda6942d093e3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>Actor 的视角</p>
<p><img src="https://juejin.cn/post/6989312701042262029" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>​</p></div>  
</div>
            