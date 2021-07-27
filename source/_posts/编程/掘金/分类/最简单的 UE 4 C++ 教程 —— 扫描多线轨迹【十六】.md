
---
title: '最简单的 UE 4 C++ 教程 —— 扫描多线轨迹【十六】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6989393105401151495'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 16:22:18 GMT
thumbnail: 'https://juejin.cn/post/6989393105401151495'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p><strong>原教程是基于 UE 4.18，我是基于 UE 4.25】</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Fsweep-multi-line-trace%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unrealcpp.com/sweep-multi-line-trace/" ref="nofollow noopener noreferrer">英文原地址</a></p>
<p>接上一节教程，本教程将说明如何使用 <strong>SweepMultiByChannel</strong> 返回给定半径内的结果。</p>
<p>创建一个新的 C++ Actor 子类并将其命名为 <strong>MySweepActor</strong> 。我们不会对默认头文件做任何修改。</p>
<p>下面是最终的头文件。</p>
<h3 data-id="heading-0">MySweepActor.h</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> once</span>

<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CoreMinimal.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"GameFramework/Actor.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"MySweepActor.generated.h"</span></span>

<span class="hljs-built_in">UCLASS</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UNREALCPP_API</span> <span class="hljs-title">AMySweepActor</span> :</span> <span class="hljs-keyword">public</span> AActor
&#123;
<span class="hljs-built_in">GENERATED_BODY</span>()

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Sets default values for this actor's properties</span>
<span class="hljs-built_in">AMySweepActor</span>();

<span class="hljs-keyword">protected</span>:
<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">BeginPlay</span><span class="hljs-params">()</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span> <span class="hljs-keyword">override</span></span>;

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989393105401151495" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在我们编写代码的逻辑之前，我们必须首先 <strong>#include DrawDebugHelpers.h</strong> 文件来帮助我们可视化 actor 。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"MySweepActor.h"</span></span>
<span class="hljs-comment">// include debug helpers</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"DrawDebugHelpers.h"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989393105401151495" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这个例子中，我们将在 <strong>BeginPlay()</strong> 函数中执行所有的逻辑。</p>
<p>首先，我们将创建一个<strong>FHitResults</strong> 的 <strong>TArray</strong>，并将其命名为 <strong>OutHits</strong>。</p>
<p>我们希望扫描球体在相同的位置开始和结束，并通过使用 <strong>GetActorLocation</strong> 使它与 actor 的位置相等。碰撞球体可以是不同的形状，在这个例子中，我们将使用 <strong>FCollisionShape:: makephere</strong> 使它成为一个球体，我们将它的半径设置为 500个虚幻单位。接下来，运行 <strong>DrawDebugSphere</strong> 来可视化扫描球体。</p>
<p>然后，我们想要设置一个名为 <strong>isHit</strong> 的 <strong>bool</strong> 变量来检查我们的扫描是否击中了任何东西。</p>
<p>我们运行 <strong>GetWorld()->SweepMultiByChannel</strong> 来执行扫描通道跟踪并返回命中情况到 <strong>OutHits</strong> 数组中。</p>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.unrealengine.com%2Flatest%2FINT%2FAPI%2FRuntime%2FEngine%2FEngine%2FUWorld%2FSweepMultiByChannel%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.unrealengine.com/latest/INT/API/Runtime/Engine/Engine/UWorld/SweepMultiByChannel/" ref="nofollow noopener noreferrer">这里</a>了解更多关于 <strong>SweepMultiByChannel</strong> 功能。如果 <strong>isHit</strong> 为真，我们将循环遍历 <strong>TArray</strong> 并打印出 hit actor 的名字和其他相关信息。</p>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.unrealengine.com%2Flatest%2FINT%2FProgramming%2FUnrealArchitecture%2FTArrays%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/TArrays/" ref="nofollow noopener noreferrer">这里</a>了解更多关于 <strong>TArray</strong> 的信息。</p>
<p>下面是最后的.cpp文件。</p>
<h3 data-id="heading-1">MySweepActor.cpp</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"MySweepActor.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"DrawDebugHelpers.h"</span></span>


<span class="hljs-comment">// Sets default values</span>
AMySweepActor::<span class="hljs-built_in">AMySweepActor</span>()
&#123;
 <span class="hljs-comment">// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.</span>
PrimaryActorTick.bCanEverTick = <span class="hljs-literal">true</span>;

&#125;

<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AMySweepActor::BeginPlay</span><span class="hljs-params">()</span>
</span>&#123;
Super::<span class="hljs-built_in">BeginPlay</span>();

<span class="hljs-comment">// create tarray for hit results</span>
TArray<FHitResult> OutHits;

<span class="hljs-comment">// start and end locations</span>
FVector SweepStart = <span class="hljs-built_in">GetActorLocation</span>();
FVector SweepEnd = <span class="hljs-built_in">GetActorLocation</span>();

<span class="hljs-comment">// create a collision sphere</span>
FCollisionShape MyColSphere = FCollisionShape::<span class="hljs-built_in">MakeSphere</span>(<span class="hljs-number">500.0f</span>);

<span class="hljs-comment">// draw collision sphere</span>
<span class="hljs-built_in">DrawDebugSphere</span>(<span class="hljs-built_in">GetWorld</span>(), <span class="hljs-built_in">GetActorLocation</span>(), MyColSphere.<span class="hljs-built_in">GetSphereRadius</span>(), <span class="hljs-number">50</span>, FColor::Purple, <span class="hljs-literal">true</span>);

<span class="hljs-comment">// check if something got hit in the sweep</span>
<span class="hljs-keyword">bool</span> isHit = <span class="hljs-built_in">GetWorld</span>()-><span class="hljs-built_in">SweepMultiByChannel</span>(OutHits, SweepStart, SweepEnd, FQuat::Identity, ECC_WorldStatic, MyColSphere);

<span class="hljs-keyword">if</span> (isHit)
&#123;
<span class="hljs-comment">// loop through TArray</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">auto</span>& Hit : OutHits)
&#123;
<span class="hljs-keyword">if</span> (GEngine) 
&#123;
<span class="hljs-comment">// screen log information on what was hit</span>
GEngine-><span class="hljs-built_in">AddOnScreenDebugMessage</span>(<span class="hljs-number">-1</span>, <span class="hljs-number">5.f</span>, FColor::Green, FString::<span class="hljs-built_in">Printf</span>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Hit Result: %s"</span>), *Hit.Actor-><span class="hljs-built_in">GetName</span>()));
<span class="hljs-comment">// uncommnet to see more info on sweeped actor</span>
<span class="hljs-comment">// GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, FString::Printf(TEXT("All Hit Information: %s"), *Hit.ToString()));</span>
&#125;
&#125;
&#125;

&#125;

<span class="hljs-comment">// Called every frame</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AMySweepActor::Tick</span><span class="hljs-params">(<span class="hljs-keyword">float</span> DeltaTime)</span>
</span>&#123;
Super::<span class="hljs-built_in">Tick</span>(DeltaTime);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6989393105401151495" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终运行的效果如下所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bc18d969abf4d058eae7dcabb0e7f1b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6989393105401151495" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​</p></div>  
</div>
            