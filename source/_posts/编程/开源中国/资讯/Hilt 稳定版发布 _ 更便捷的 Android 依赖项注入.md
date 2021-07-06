
---
title: 'Hilt 稳定版发布 _ 更便捷的 Android 依赖项注入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/07/9GMvK9.png'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 15:46:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/07/9GMvK9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/07/9GMvK9.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection%2Fhilt-android" target="_blank">Hilt</a> 是 Jetpack 推荐使用的 Android 应用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection" target="_blank">依赖项注入 (DI)</a> 解决方案，现已 <strong>稳定</strong>。这意味着 Hilt 已经完全可以在 <strong>生产环境</strong> 中使用。Hilt 相比 Dagger 更加便捷，同时也能帮您减少模板代码，它专为 Android 而生，并集成了多个 Jetpack 依赖库。很多公司已在他们的应用中使用了 Hilt 并从中获益。</p> 
<p>2020 年 6 月，Hilt <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fandroiddevelopers%2Fdependency-injection-on-android-with-hilt-67b6031e62d" target="_blank">首次发布</a> 预览版，它肩负着定义 Android 依赖项注入 <strong>标准方案</strong> 的使命，也是自那时起，我们收到了来自开发者的海量反馈。这些反馈不仅改善了 Hilt，而且使我们明确了我们走在正确的道路上。</p> 
<p>Hilt 无需手动创建依赖项关系图，也无需手动注入并传递类型，而是在编译期自动根据注解生成所需代码。Hilt 通过实现工作中的复杂部分以及<strong>生成所有模板代码</strong>替代手动编写，帮您<strong>从 DI 的最佳实践中获得最大收益</strong>。此外，Hilt 与 Android 完全集成，可以帮助您自动管理 Android Framework 类的依赖项关系图的生命周期。</p> 
<p>让我们通过一个简单示例观察 Hilt 的行为！<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection%2Fhilt-android%23setup" target="_blank">配置 Hilt 之后</a>，在项目中从无到有地向 Activity 注入ViewModel 就像在代码中添加注解一样容易，如下所示:</p> 
<pre><code>@HiltAndroidApp // 在应用中配置 Hilt
class MyApplication : Application() &#123; ... &#125;

// 使 Hilt 识别该 ViewModel
@HiltViewModel
class LoginViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle,
    /*…Hilt 关注的其他依赖项... */
) : ViewModel() &#123; ... &#125;


// 使该 Activity 使用正确的 ViewModel 工厂，并注入其他依赖项
@AndroidEntryPoint 
class LoginActivity : AppCompatActivity() &#123;

    private val loginViewModel: LoginViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        // loginViewModel 已经可以使用
    &#125;
&#125;
</code></pre> 
<p>除了上述内容，让您在应用中选择使用 Hilt 还有哪些理由呢？</p> 
<h2><strong>比 Dagger 更便捷</strong></h2> 
<p>Hilt 基于流行的 DI 库 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection%2Fdagger-basics" target="_blank">Dagger</a> 构建，因此可以从 Dagger 提供的编译期校验、良好的运行时性能、扩展性以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F270185205" target="_blank">Android Studio 支持</a> 中受益。一些 Dagger 注解也常用于 Hilt，例如 <a href="https://my.oschina.net/u/4027648">@Inject</a> (告知 Dagger/Hilt 如何提供一个类型的实例)。但是 Hilt 要比 Dagger 更便捷。</p> 
<blockquote> 
 <p><em>我强烈推荐利用 Dagger 在 Android 应用中进行依赖项注入，然而单纯地使用 Dagger 可能导致在创建时内存占用过多。当这与 Android 开发中各种复杂的可感知生命周期组件一起使用时，就可能出现很多陷阱，例如内存泄漏: 作用域为 Activity 的依赖项被意外地传递到 ViewModel 中。专为 Android 量身定制的 Hilt 可以帮助您避开 Dagger 基本使用的一些陷阱。</em></p> 
 <p>——Tinder 资深软件工程师 Marcelo Hernandez</p> 
</blockquote> 
<p>如果您已经在应用中使用了 Dagger，并且希望迁移到 Hilt，无需担心！Dagger 和 Hilt 可以共存，应用可以基于需要进行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdagger.dev%2Fhilt%2Fmigration-guide" target="_blank">迁移</a>。</p> 
<h2><strong>更少的模板代码</strong></h2> 
<p>Hilt 是被定制过的——这意味着为了减少您编写代码，它替您做了一些决定。Hilt 定义了标准组件及依赖关系图，并且完全集成了 Android Framework 中的类，例如: Application、Activity、Fragment、View，还定义了限制类型实例的作用域到这些组件的作用域注解。</p> 
<blockquote> 
 <p><em>通过 @HiltAndroidTest 注解，Hilt 可以自动生成测试应用以及测试组件。迁移到 Hilt 之后，我们可以删除 20% - 40% 的测试相关模板代码。</em></p> 
 <p>——YouTube 软件工程师 Jusun Lee</p> 
</blockquote> 
<blockquote> 
 <p><em>我们仅是在 Hilt 迁移上做了浅层工作。然而，我们在其中一个迁移到 Hilt 的模块，看到了代码行数 +72/-182 的变化。</em></p> 
 <p>——Tinder 资深软件工程师 Marcelo Hernandez</p> 
</blockquote> 
<h2><strong>为 Android 量身定制</strong></h2> 
<p>不同于 Java 编程语言应用的依赖项注入解决方案 Dagger，Hilt 仅支持 Android 应用。一些注解专供 Hilt 使用，并定义了专有的 Android DI 方式，这些注解包括: <code>@HiltAndroidApp</code>、<code>@AndroidEntryPoint</code>、<code>@HiltViewModel</code>。</p> 
<blockquote> 
 <p><em>最终，Hilt 提供了内置的可识别 Android 生命周期的 Dagger 组件。使用 Hilt，我们可以只关注 Dagger <a href="https://my.oschina.net/modules">@Modules</a>，而不必担心组件，子组件以及组件提供程序的模式等。</em></p> 
 <p>—— Tinder 资深软件工程师 Marcelo Hernandez</p> 
</blockquote> 
<h2><strong>组件及绑定的标准化</strong></h2> 
<p>不同于对 Dagger 的认识，Hilt 采用了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdagger.dev%2Fhilt%2Fmonolithic" target="_blank">单组件系统</a> 来简化依赖项关系图，使编译期生成更少的代码。</p> 
<blockquote> 
 <p><em>通过 Hilt 的单组件系统，仅一次提供绑定定义，就可以在所有使用该组件的类中共享。这比之前有着很大的提升，YouTube 曾使用多组件系统，模块需要手动连接到自定义组件中，并且存在很多重复的绑定定义。</em></p> 
 <p>——YouTube 软件工程师 Jusun Lee</p> 
</blockquote> 
<blockquote> 
 <p><em>由于我们的 Gradle 模块分离允许隔离开发功能，这使得我们使用 Dagger 时容易过于灵活。我们发现，将这些模块迁移到 Hilt 暴露出我们无意间违反了关注点分离的缺陷。</em></p> 
 <p>——Tinder 资深软件开发工程师 Marcelo Hernandez</p> 
</blockquote> 
<h2><strong>集成其他 Jetpack 库</strong></h2> 
<p>您可以在开箱即用的情况下使用喜欢的 Jetpack 库。到目前为止，我们为 <strong>ViewModel</strong>、<strong>WorkManager</strong>、<strong>Navigation</strong> 和 <strong>Compose</strong> 提供直接注入支持。</p> 
<p>参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection%2Fhilt-jetpack" target="_blank">文档</a>，了解更多关于 Jetpack 的支持。</p> 
<blockquote> 
 <p><em>我非常感激 Hilt 与 ViewModel 一起开箱即用的使用方式，以及它消除单纯使用 Dagger 时必须设置的 ViewModel.Factory 模板代码的方式。</em></p> 
 <p>——Tinder 资深软件开发工程师 Marcelo Hernandez</p> 
</blockquote> 
<h2><strong>Hilt 学习资源</strong></h2> 
<p>Hilt 是 Jetpack 推荐的 Android 应用 DI 解决方案。想要了解更多并开始在您的应用中使用，请参阅如下资源:</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection" target="_blank">了解使用依赖项注入的收益</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fdependency-injection%2Fhilt-android" target="_blank">了解如何在您的应用中使用 Hilt</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdagger.dev%2Fhilt%2Fmigration-guide" target="_blank">从 Dagger 到 Hilt 的迁移指南</a></p> </li> 
 <li> <p>Codelabs 中逐步学习 Hilt 教程:</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fcodelabs%2Fandroid-hilt%230" target="_blank">在 Android 应用中使用 Hilt</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fcodelabs%2Fandroid-dagger-to-hilt%230" target="_blank">将 Dagger 应用迁移到 Hilt</a></li> 
  </ul> </li> 
 <li> <p>代码示例:</p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fiosched" target="_blank">Google I/O 2020 应用</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandroid%2Fsunflower" target="_blank">Sunflower 应用</a></li> 
  </ul> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fservices.google.cn%2Ffh%2Ffiles%2Fmisc%2Fhilt-annotations-2.3.3_zh-cn.pdf" target="_blank">Hilt 及 Dagger 注解的区别及使用方式的备忘录</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            