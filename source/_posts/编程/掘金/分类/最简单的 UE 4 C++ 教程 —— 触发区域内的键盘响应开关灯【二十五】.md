
---
title: '最简单的 UE 4 C++ 教程 —— 触发区域内的键盘响应开关灯【二十五】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6990179347608895501'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:07:04 GMT
thumbnail: 'https://juejin.cn/post/6990179347608895501'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p><strong>原教程是基于 UE 4.18，我是基于 UE 4.25】</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Flight-switch-push-button%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unrealcpp.com/light-switch-push-button/" ref="nofollow noopener noreferrer">英文原地址</a></p>
<p>接上一节教程，创建一个新的 C++ Actor 子类并将其命名为 <strong>LightSwitchPushButton</strong> 。我们将在头文件中定义四个东西 —— 我们将定义一个 <strong>UPointLightComponent</strong>、<strong>USphereComponent</strong>、<strong>float</strong> 变量和 <strong>void</strong> 函数。</p>
<p>下面是最终的头代码。</p>
<h3 data-id="heading-0">LightSwitchPushButton.h</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> once</span>

<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CoreMinimal.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"GameFramework/Actor.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"LightSwitchPushButton.generated.h"</span></span>

<span class="hljs-built_in">UCLASS</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UNREALCPP_API</span> <span class="hljs-title">ALightSwitchPushButton</span> :</span> <span class="hljs-keyword">public</span> AActor
&#123;
<span class="hljs-built_in">GENERATED_BODY</span>()

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Sets default values for this actor's properties</span>
<span class="hljs-built_in">ALightSwitchPushButton</span>();

<span class="hljs-keyword">protected</span>:
<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">virtual</span> <span class="hljs-keyword">void</span> <span class="hljs-title">BeginPlay</span><span class="hljs-params">()</span> <span class="hljs-keyword">override</span></span>;

<span class="hljs-keyword">public</span>:
<span class="hljs-comment">// Called every frame</span>
<span class="hljs-comment">// virtual void Tick(float DeltaTime) override;</span>

<span class="hljs-comment">// declare point light comp</span>
<span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere, Category = <span class="hljs-string">"Light Switch"</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UPointLightComponent</span>* <span class="hljs-title">PointLight</span>;</span>

<span class="hljs-comment">// declare sphere comp</span>
<span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere, Category = <span class="hljs-string">"Light Switch"</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">USphereComponent</span>* <span class="hljs-title">LightSphere</span>;</span>

<span class="hljs-comment">// declare light intensity variable</span>
<span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere, Category = <span class="hljs-string">"Light Switch"</span>)
<span class="hljs-keyword">float</span> LightIntensity;

<span class="hljs-comment">// declare ToggleLight function</span>
<span class="hljs-built_in">UFUNCTION</span>(BlueprintCallable, Category = <span class="hljs-string">"Light Switch"</span>)
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ToggleLight</span><span class="hljs-params">()</span></span>;

&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，在我们的 .cpp 文件中，让我们首先 #include 我们将在代码中使用的必要脚本。包括<strong>Components / PointLightComponent.h</strong> 和 <strong>Components/ spherecomcomponent .h</strong> 两个文件。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"LightSwitchPushButton.h"</span></span>
<span class="hljs-comment">// include these header files</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Components/PointLightComponent.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Components/SphereComponent.h"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将在构造函数中设置 actor 的所有默认属性。首先让我们设置我们的 float 变量 <strong>LightIntensity</strong> 为 3000.0f，它将使光相对于其他对象看起来足够明亮。接下来，我们将创建我们的<strong>UPointLightComponent</strong> 并将它设置为我们的 <strong>RootComponent</strong> 。之后，我们将创建<strong>USphereComponent</strong>，当我们的玩家在半径内时，它将作为碰撞球体。然后，我们将创建简单的<strong>ToggleLight()</strong> 函数来切换灯光的可见性状态。稍后我们将从玩家代码中调用该函数。下面是<strong>LightSwitchPushButton</strong> 角色的最后一个 .cpp 文件。</p>
<h3 data-id="heading-1">LightSwitchPushButton.cpp</h3>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"LightSwitchPushButton.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Components/PointLightComponent.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"Components/SphereComponent.h"</span></span>

<span class="hljs-comment">// Sets default values</span>
ALightSwitchPushButton::<span class="hljs-built_in">ALightSwitchPushButton</span>()
&#123;
 <span class="hljs-comment">// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.</span>
PrimaryActorTick.bCanEverTick = <span class="hljs-literal">true</span>;

LightIntensity = <span class="hljs-number">3000.0f</span>;

PointLight = CreateDefaultSubobject<UPointLightComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Point Light"</span>));
PointLight->Intensity = LightIntensity;
<span class="hljs-comment">//PointLight->bVisible = true; ///< 过时了</span>
    <span class="hljs-comment">//PointLight->SetVisibleFlag(true);</span>
    PointLight-><span class="hljs-built_in">SetVisibility</span>(<span class="hljs-literal">true</span>);
RootComponent = PointLight;

LightSphere = CreateDefaultSubobject<USphereComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Light Sphere Component"</span>));
LightSphere-><span class="hljs-built_in">InitSphereRadius</span>(<span class="hljs-number">300.0f</span>);
LightSphere-><span class="hljs-built_in">SetCollisionProfileName</span>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Trigger"</span>));
LightSphere-><span class="hljs-built_in">SetCollisionResponseToChannel</span>(ECC_Pawn, ECR_Ignore);
LightSphere-><span class="hljs-built_in">SetupAttachment</span>(RootComponent);
&#125;

<span class="hljs-comment">// Called when the game starts or when spawned</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ALightSwitchPushButton::BeginPlay</span><span class="hljs-params">()</span>
</span>&#123;
Super::<span class="hljs-built_in">BeginPlay</span>();
&#125;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">ALightSwitchPushButton::ToggleLight</span><span class="hljs-params">()</span>
</span>&#123;
    PointLight-><span class="hljs-built_in">ToggleVisibility</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，和上一节类似，让我们向项目添加一个 <strong>Action</strong> 输入。在本例中，我们将把 <strong>Action</strong> 输入绑定到键盘的 <strong>F</strong>键。转到 <strong>编辑>项目设置 ( Edit > Project Settings</strong>)。然后选择 Input 选项。单击 <strong>Action Mappings</strong> 旁边的加号。调用新的输入 <strong>Action</strong> 并从下拉菜单中选择 <strong>F</strong> 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6066b1a979c4e8f9ed2738c6834c8e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6353b30b9c1427997b14427ab36d99c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>【<strong>以下我们把目光转到 xxxCharacter.h / .cpp 上</strong>】 </p>
<p> 在 xxxCharacter.h文件中，在 <strong>OnFire</strong> 方法下添加 <strong>OnAction</strong> 方法。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">protected</span>:

<span class="hljs-comment">/** Fires a projectile. */</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">OnFire</span><span class="hljs-params">()</span></span>;

<span class="hljs-comment">// on action </span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">OnAction</span><span class="hljs-params">()</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外，我们还必须包含 <strong>LightSwitchPushButton</strong> 头文件，这样我们的角色才能访问它的功能。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"CoreMinimal.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"GameFramework/Character.h"</span></span>
<span class="hljs-comment">// include our new LightSwitchPushButton header file</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"LightSwitchPushButton/LightSwitchPushButton.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"UnrealCPPCharacter.generated.h"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后为玩家当前重叠的灯开关声明一个变量 <strong>CurrentLightSwitch</strong> 。此外，我们还需要声明重叠事件，来使得当玩家处于光的球体组件的半径内时，触发我们想要运行的函数。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// declare overlap begin function</span>
<span class="hljs-built_in">UFUNCTION</span>()
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">OnOverlapBegin</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, <span class="hljs-keyword">bool</span> bFromSweep, <span class="hljs-keyword">const</span> FHitResult& SweepResult)</span></span>;

<span class="hljs-comment">// declare overlap end function</span>
<span class="hljs-built_in">UFUNCTION</span>()
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">OnOverlapEnd</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex)</span></span>;
<span class="hljs-comment">// declare current light switch</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ALightSwitchPushButton</span>* <span class="hljs-title">CurrentLightSwitch</span>;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> 同时还声明了 <strong><code>UCapsuleComponent</code></strong> 来处理我们的触发事件</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-built_in">UPROPERTY</span>(VisibleAnywhere, Category = <span class="hljs-string">"Trigger Capsule"</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UCapsuleComponent</span>* <span class="hljs-title">TriggerCapsule</span>;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在构造函数中添加触发器胶囊并将其绑定到重叠事件。接着设置变量 <strong>CurrentLightSwitch</strong> 为<strong>NULL</strong>。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">AUnrealCPPCharacter::<span class="hljs-built_in">AUnrealCPPCharacter</span>()
&#123;
    ...
    <span class="hljs-comment">// create trigger capsule</span>
    TriggerCapsule = CreateDefaultSubobject<UCapsuleComponent>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Trigger Capsule"</span>));
    TriggerCapsule-><span class="hljs-built_in">InitCapsuleSize</span>(<span class="hljs-number">55.f</span>, <span class="hljs-number">96.0f</span>);;
    TriggerCapsule-><span class="hljs-built_in">SetCollisionProfileName</span>(<span class="hljs-built_in">TEXT</span>(<span class="hljs-string">"Trigger"</span>));
    TriggerCapsule-><span class="hljs-built_in">SetupAttachment</span>(RootComponent);

    <span class="hljs-comment">// bind trigger events</span>
    TriggerCapsule->OnComponentBeginOverlap.<span class="hljs-built_in">AddDynamic</span>(<span class="hljs-keyword">this</span>, &AUnrealCPPCharacter::OnOverlapBegin); 
    TriggerCapsule->OnComponentEndOverlap.<span class="hljs-built_in">AddDynamic</span>(<span class="hljs-keyword">this</span>, &AUnrealCPPCharacter::OnOverlapEnd); 

     <span class="hljs-comment">// set current light switch to null</span>
     CurrentLightSwitch = <span class="hljs-literal">NULL</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>进一步，将 <strong>Action</strong> 输入绑定连接到玩家</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AUnrealCPPCharacter::SetupPlayerInputComponent</span><span class="hljs-params">(class UInputComponent* PlayerInputComponent)</span>
</span>&#123;
    ...
    <span class="hljs-comment">// Bind action event</span>
    PlayerInputComponent-><span class="hljs-built_in">BindAction</span>(<span class="hljs-string">"Action"</span>, IE_Pressed, <span class="hljs-keyword">this</span>, &AUnrealCPPCharacter::OnAction);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将 <strong>OnAction()</strong> 函数添加到玩家脚本中。该函数将检查 <strong>CurrentLightSwitch</strong> 是否为 <strong>NULL</strong> 。如果<strong>CurrentLightSwitch</strong> 不为 <strong>NULL</strong>，那么当玩家按下动作键 F 时，将切换灯光的可见性（开关灯）。然后，添加重叠函数来设置和取消 <strong>CurrentLightSwitch</strong></p>
<p> </p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AUnrealCPPCharacter::OnAction</span><span class="hljs-params">()</span> 
</span>&#123;
<span class="hljs-keyword">if</span>(CurrentLightSwitch) 
&#123;
CurrentLightSwitch-><span class="hljs-built_in">ToggleLight</span>();
&#125;
&#125;

<span class="hljs-comment">// overlap on begin function</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AUnrealCPPCharacter::OnOverlapBegin</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, <span class="hljs-keyword">bool</span> bFromSweep, <span class="hljs-keyword">const</span> FHitResult& SweepResult)</span>
</span>&#123;
<span class="hljs-keyword">if</span> (OtherActor && (OtherActor != <span class="hljs-keyword">this</span>) && OtherComp && OtherActor-><span class="hljs-built_in">GetClass</span>()-><span class="hljs-built_in">IsChildOf</span>(ALightSwitchPushButton::<span class="hljs-built_in">StaticClass</span>())) 
&#123;
CurrentLightSwitch = Cast<ALightSwitchPushButton>(OtherActor);
&#125;
&#125; 

<span class="hljs-comment">// overlap on end function</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">AUnrealCPPCharacter::OnOverlapEnd</span><span class="hljs-params">(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex)</span>
</span>&#123;
<span class="hljs-keyword">if</span> (OtherActor && (OtherActor != <span class="hljs-keyword">this</span>) && OtherComp) 
&#123;
CurrentLightSwitch = <span class="hljs-literal">NULL</span>;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译代码。拖放 actor （<strong>LightSwitchPushButton</strong>）到场景中，当玩家进入球形触发区域，点击 <strong>F</strong> 键开关灯。</p>
<p>最后的效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b96cdec996a0422f960dcb0f7889f674~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6990179347608895501" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>\</p>
<p>​</p></div>  
</div>
            