
---
title: 'Taro v3.5 正式发布：开发体验提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://storage.360buyimg.com/cjj-pub-images/mini-speed.jpeg'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 15:04:00 GMT
thumbnail: 'https://storage.360buyimg.com/cjj-pub-images/mini-speed.jpeg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div style="margin-left:0px">
  距离 Taro 3.5 的 Beta 版本发布已有两个月的时间，期间我们在不断地对基于 Webpack5 的编译系统、基于 Next.js 的 SSR 等功能进行打磨的同时，新增了对 pnpm 的支持等新功能。此外 Taro 社区也有很多同学参与共建，如 Taro 合作者
  <span> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbiorz" target="_blank">@biorz</a>
  <span> </span>为 ReactNative 侧贡献了重要特性：支持把 Taro 组件编译为 RN 组件。
 </div> 
</div> 
<div style="text-align:start"> 
 <p>日前 Taro v3.5 已正式发布，下文将介绍关于 3.5 的主要特性与重要修复，以及后续的版本规划。</p> 
 <h2>一、编译提速<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E4%25B8%2580%25E7%25BC%2596%25E8%25AF%2591%25E6%258F%2590%25E9%2580%259F" target="_blank">​</a></h2> 
 <p>Taro v3.5 基于 Webpack5 构建了新的编译系统，利用持久化缓存、依赖预编译、SWC 等方法与工具，大幅降低了编译所需耗时。开发者可以自由选择切换使用 Webpack5 进行编译，也可以继续保持使用 Webpack4，另外在 v3.6 中 Taro 还将支持使用 Vite 进行编译。</p> 
 <blockquote> 
  <p>依赖预编译可以预先把项目的第三方依赖打包为一个模块联邦 remote 应用，再次编译时 Webpack 无需再对这些依赖进行编译，从而提升编译速度。关于 Webpack5 编译系统的实现细节，请浏览 《Taro v3.5 beta 编译提速》</p> 
 </blockquote> 
 <p>v3.5 Beta 发布后，我们补全了 H5 端的依赖预编译功能，并且把依赖预编译作为一个通用能力提取了出来。可供 Taro 以外的使用 Webpack5 的 H5 项目使用，通过<span> </span><code>@tarojs/webpack5-prebundle</code><span> </span>进行编译提速，具体使用方法可参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fprebundle%23%25E7%25AC%25AC%25E4%25B8%2589%25E6%2596%25B9%25E6%258E%25A5%25E5%2585%25A5" target="_blank">相关文档</a>。</p> 
 <h3>提速效果<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E6%258F%2590%25E9%2580%259F%25E6%2595%2588%25E6%259E%259C" target="_blank">​</a></h3> 
 <p>以<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui%2Ftree%2Fnext%2Fsrc%2Fsites%2Fmobile-taro%2Fvue" target="_blank">NutUI 组件示例库</a><span> </span>为例，小程序、H5 端的编译速度测试结果如下：</p> 
 <p><strong>小程序：</strong></p> 
 <p><img alt="GroupBar-20220725.jpeg" src="https://storage.360buyimg.com/cjj-pub-images/mini-speed.jpeg" referrerpolicy="no-referrer"></p> 
 <p><strong>H5：</strong></p> 
 <p><img alt="GroupBar-20220725 (1).jpeg" src="https://storage.360buyimg.com/cjj-pub-images/web-speed.jpeg" referrerpolicy="no-referrer"></p> 
 <p>使用方法</p> 
 <p>简单修改 Taro 的编译配置即可切换使用 Webpack4 或 Webpack5 进行编译：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>/** config/index.js */</em>
</span><span style="color:#393a34"><span style="color:#00009f">const</span><span> config </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><em>// 自定义编译工具，可选 'Webpack4' 或 'Webpack5'</em>
</span><span style="color:#393a34"><span>  </span><span style="color:#36acaa">compiler</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'webpack4'</span><span> </span><span style="color:#393a34">||</span><span> </span><span style="color:#e3116c">'webpack5'</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span>
</span>
</code></pre> 
  </div> 
 </div> 
 <h2>二、RN<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E4%25BA%258Crn" target="_blank">​</a></h2> 
 <h3>1. React Native 0.68 版本支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%231-react-native-068-%25E7%2589%2588%25E6%259C%25AC%25E6%2594%25AF%25E6%258C%2581" target="_blank">​</a></h3> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fblog%2F2022%2F03%2F30%2Fversion-068" target="_blank">React Native 0.68 版本已于 2022-3-30 正式发布</a>。0.68 是首个可选接入 New Architecture 的版本，新架构有望为 RN 带来性能和体验上的飞跃。Taro 默认选择的 RN 版本，正式切换到了 0.68，开发者通过<span> </span><code>taro init</code><span> </span>选择<span> </span><code>react-native</code><span> </span>模板即可。</p> 
 <p>另外 0.69 版本的适配，也在进展中。</p> 
 <h3>2. RN<span> </span><strong>相关依赖库由 unimodules 升级至 expo</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%232-rn-%25E7%259B%25B8%25E5%2585%25B3%25E4%25BE%259D%25E8%25B5%2596%25E5%25BA%2593%25E7%2594%25B1-unimodules-%25E5%258D%2587%25E7%25BA%25A7%25E8%2587%25B3-expo" target="_blank">​</a></h3> 
 <p>Expo 是 React Native 生态中的重要角色，提供了非常多优秀的模块，在 Taro 中有较为广泛的使用，如 expo-av、expo-camera 等，将来我们还会持续接入新的模块。Expo 的模块系统，由 unimodules 变更为 expo 已有一段时日，其架构变更原因可参考文章： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.expo.dev%2Fwhats-new-in-expo-modules-infrastructure-7a7cdda81ebc" target="_blank">What’s new in Expo modules infrastructure</a>。</p> 
 <p>Taro v3.5 及以后将使用新的模块系统，后续壳工程不再包含 unimodules 版本。旧版本升级可参考此<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-native-shell%2Fpull%2F72" target="_blank">PR</a>，升级过程较为繁琐，建议重新 init 一个仓库，再将业务改动同步。升级为 expo 后，不再支持 iOS 11，详细内容请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2F11565" target="_blank">discussions</a>。</p> 
 <h3>3.<span> </span><strong>支持把 Taro 组件编译为 React Native 组件</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%233-%25E6%2594%25AF%25E6%258C%2581%25E6%258A%258A-taro-%25E7%25BB%2584%25E4%25BB%25B6%25E7%25BC%2596%25E8%25AF%2591%25E4%25B8%25BA-react-native-%25E7%25BB%2584%25E4%25BB%25B6" target="_blank">​</a></h3> 
 <p>如果您想在现存的 React Native 项目中(非 Taro RN )，复用您的 Taro 组件，那么这个新功能或许适合您。</p> 
 <p>您可以使用以下命令编译组件，编译后的组件产物可以直接在 React Native 项目中使用。 详细内容请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2F11860" target="_blank">discussions</a>。</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>taro build native-components --type rn</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>4. 编译打包方案优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%234-%25E7%25BC%2596%25E8%25AF%2591%25E6%2589%2593%25E5%258C%2585%25E6%2596%25B9%25E6%25A1%2588%25E4%25BC%2598%25E5%258C%2596" target="_blank">​</a></h3> 
 <p>Android 的打包过程，从调用 gradlew 改为使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.fastlane.tools%2F" target="_blank">fastlane</a>，将打包过程配置化，尽可能地减少对 RN 初始化后原生代码的入侵。相关配置位于 <code>android/fastlane</code>，目前仅做了基础配置，开发者可进一步自定义。</p> 
 <p>刚接触 Taro 开发 APP 的开发者，经常在开发环境的配置上，消耗大量时间。再次建议大家先学习利用 GitHub Action 进行打包编译，相关代码位于<span> </span><code>.github</code><span> </span>目录中。</p> 
 <h3>5. 调试工具 Taro Playground 升级至 Taro 3.5 版本及 React Native 0.68<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%235-%25E8%25B0%2583%25E8%25AF%2595%25E5%25B7%25A5%25E5%2585%25B7-taro-playground-%25E5%258D%2587%25E7%25BA%25A7%25E8%2587%25B3-taro-35-%25E7%2589%2588%25E6%259C%25AC%25E5%258F%258A-react-native-068" target="_blank">​</a></h3> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwuba%2Ftaro-playground" target="_blank">Taro Playground</a><span> </span>作为 Taro RN 端的调试工具及跨端 Demo，进行了同步更新。此次更新无法保证向下兼容，使用旧版本 Taro 的开发者，如需调试 Android，可在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwuba%2Ftaro-playground%2Freleases" target="_blank">releases</a><span> </span>中下载旧包进行调试。在 App Store 中，我们只上架最新版本，需要旧版本的开发者请不要开启应用自动更新。如不慎升级，需自行打包编译，或联系我们加入测试组。</p> 
 <h3>6. 壳工程代码整理<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%236-%25E5%25A3%25B3%25E5%25B7%25A5%25E7%25A8%258B%25E4%25BB%25A3%25E7%25A0%2581%25E6%2595%25B4%25E7%2590%2586" target="_blank">​</a></h3> 
 <p>对于 0.68 版本的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-native-shell%2Ftree%2F0.68.0" target="_blank">壳工程</a>，我们进行了代码的重新整理。将初始化 RN、安装 expo、兼容 Taro、安装依赖、添加Github Action，每一个步骤一一列出，方便开发者在定制壳工程时进行参考。</p> 
 <h2>三、pnpm<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E4%25B8%2589pnpm" target="_blank">​</a></h2> 
 <p>众所周知，pnpm 在当下被誉为“最先进的包管理工具”，它是由 npm/yarn 衍生而来，解决了 npm/yarn 内部潜在的 bug，极大的优化了性能，扩展了使用场景。在社区内很高的呼声下，Taro 也在提供了这一热门的包管理工具选项。</p> 
 <p>在 Taro v3.5 版本以后，在脚手架内置包管理工具不再自动识别本地环境内安装的包管理工具，而是需要开发者自行选择需要的包管理工具，供开发者更方便使用和操作。</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>? 请选择包管理工具 </span><span style="color:#393a34">(</span><span>Use arrow keys</span><span style="color:#393a34">)</span>
</span><span style="color:#393a34"><span>❯ </span><span style="color:#d73a49">yarn</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#d73a49">pnpm</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#d73a49">npm</span>
</span><span style="color:#393a34"><span>  cnpm</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>如果是在较旧的 Taro 项目中，想使用 pnpm 管理工具，由于<strong>幽灵依赖</strong>的存在，开发者需要在项目中手动安装并升级依赖来修复该问题，具体操作可参考文中<code>升级指南</code>第 5 项。</p> 
 <h2>四、其它特性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E5%259B%259B%25E5%2585%25B6%25E5%25AE%2583%25E7%2589%25B9%25E6%2580%25A7" target="_blank">​</a></h2> 
 <p>除了以上新特性外，v3.5 还包括很多重要的更新：</p> 
 <h3>1. 适配 React 18<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%231-%25E9%2580%2582%25E9%2585%258D-react-18" target="_blank">​</a></h3> 
 <p>从 Taro v3.5 开始，Taro 将默认使用 React 18 版本。你可以在 Taro 使用 React18 中激动人心的新特性了。从新建项目开始探索吧：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em># @tarojs/cli 升级到 v3.5</em>
</span><span style="color:#393a34"><span>$ taro init myProject</span>
</span><span style="color:#393a34"><em># 选择「react」框架</em>
</span></code></pre> 
  </div> 
 </div> 
 <p>需要注意的是，受小程序环境限制，诸如新 Suspense 特性将不能在小程序中使用，详情请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Freact-18" target="_blank">浏览文档</a>。</p> 
 <h3>2. H5 支持服务端渲染<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%232-h5-%25E6%2594%25AF%25E6%258C%2581%25E6%259C%258D%25E5%258A%25A1%25E7%25AB%25AF%25E6%25B8%25B2%25E6%259F%2593" target="_blank">​</a></h3> 
 <p>通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSyMind%2Ftarojs-plugin-platform-nextjs" target="_blank">tarojs-plugin-platform-nextjs</a><span> </span>插件配置，我们可以将 Taro 和 nextjs 社区生态打通，让 Taro H5 支持 Pre-rendering（预渲染）、SSR（服务端渲染）和 ISR（增量静态生成）各种特性，提升页面首屏渲染速度🚀，也利于 SEO 优化🔍。</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> </span><span style="color:#d73a49">install</span><span> tarojs-plugin-platform-nextjs next</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>在 Taro 项目的 <code>config/index.js</code><span> </span>中添加插件。</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#00009f">const</span><span> config </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#36acaa">plugins</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">[</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#e3116c">'tarojs-plugin-platform-nextjs'</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">]</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>启动项目。</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span>npx taro build --type nextjs --watch</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>插件来自社区大佬<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSyMind" target="_blank">@SyMind</a><span> </span>贡献，详细用法可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSyMind%2Ftarojs-plugin-platform-nextjs" target="_blank">插件文档</a>。</p> 
 <h3>3. H5 支持多页应用模式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%233-h5-%25E6%2594%25AF%25E6%258C%2581%25E5%25A4%259A%25E9%25A1%25B5%25E5%25BA%2594%25E7%2594%25A8%25E6%25A8%25A1%25E5%25BC%258F" target="_blank">​</a></h3> 
 <p>H5 端的多页应用模式是社区呼声最高的若干特性之一，在新版本中将得到支持，详细用法及注意事项请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fdocs%2Fnext%2Fconfig-detail%23h5routermode" target="_blank">参考文档</a>。</p> 
 <p>配置开启多页应用模式：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>/** config/index.js */</em>
</span><span style="color:#393a34"><span style="color:#00009f">const</span><span> config </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#36acaa">h5</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#36acaa">router</span><span style="color:#393a34">:</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>      </span><span style="color:#36acaa">mode</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'multi'</span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#393a34">&#125;</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>4. 补全对小程序生命周期方法的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%234-%25E8%25A1%25A5%25E5%2585%25A8%25E5%25AF%25B9%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E6%2596%25B9%25E6%25B3%2595%25E7%259A%2584%25E6%2594%25AF%25E6%258C%2581" target="_blank">​</a></h3> 
 <p>过去 Taro 对于小程序常用的生命周期方法支持得不够完整，新版本中将补全对应的方法与钩子。</p> 
 <p><strong>新增 App 生命周期：</strong></p> 
 <ul> 
  <li>onError（React & Vue3）</li> 
 </ul> 
 <p><strong>新增钩子：</strong></p> 
 <ul> 
  <li>useLaunch（React）</li> 
  <li>useError（React）</li> 
  <li>usePageNotFound（React）</li> 
  <li>useLoad（React & Vue3）</li> 
  <li>useUnload（React & Vue3）</li> 
  <li>useSaveExitState（React & Vue3）</li> 
 </ul> 
 <h3>5. 小程序内部实现优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%235-%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E5%2586%2585%25E9%2583%25A8%25E5%25AE%259E%25E7%258E%25B0%25E4%25BC%2598%25E5%258C%2596" target="_blank">​</a></h3> 
 <p>对小程序的内部实现进行优化，减少约 50k 包体积，同时降低内存占用，减少 setData 发送的数据量。</p> 
 <h2>五、升级指南<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E4%25BA%2594%25E5%258D%2587%25E7%25BA%25A7%25E6%258C%2587%25E5%258D%2597" target="_blank">​</a></h2> 
 <h3>1. 升级 Taro CLI<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%231-%25E5%258D%2587%25E7%25BA%25A7-taro-cli" target="_blank">​</a></h3> 
 <p>升级全局的 Taro CLI：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i -g @tarojs/cli</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>或升级本地的 Taro CLI 工具：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @tarojs/cli</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>2. 更新项目依赖<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%232-%25E6%259B%25B4%25E6%2596%25B0%25E9%25A1%25B9%25E7%259B%25AE%25E4%25BE%259D%25E8%25B5%2596" target="_blank">​</a></h3> 
 <blockquote> 
  <p>如果依赖安装失败或安装成功却运行报错，可以尝试删除 node_modules、yarn.lock、package-lock.json、pnpm-lock.yaml 后重新安装依赖。</p> 
 </blockquote> 
 <h3>2.1 更新项目内的 Taro 相关依赖<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%2321-%25E6%259B%25B4%25E6%2596%25B0%25E9%25A1%25B9%25E7%259B%25AE%25E5%2586%2585%25E7%259A%2584-taro-%25E7%259B%25B8%25E5%2585%25B3%25E4%25BE%259D%25E8%25B5%2596" target="_blank">​</a></h3> 
 <p>把<span> </span><code>package.json</code><span> </span>中 Taro 相关依赖的版本修改为<span> </span><code>3.5.0</code><span> </span>后重新安装依赖。</p> 
 <h3>2.2 使用 React 的项目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%2322-%25E4%25BD%25BF%25E7%2594%25A8-react-%25E7%259A%2584%25E9%25A1%25B9%25E7%259B%25AE" target="_blank">​</a></h3> 
 <ul> 
  <li>*【Breaking】**使用 React 的项目需要额外安装<span> </span><code>@pmmmwh/react-refresh-webpack-plugin</code><span> </span>和<span> </span><code>react-refresh</code>：</li> 
 </ul> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @pmmmwh/react-refresh-webpack-plugin react-refresh --save-dev</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>2.3 使用 PReact 的项目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%2323-%25E4%25BD%25BF%25E7%2594%25A8-preact-%25E7%259A%2584%25E9%25A1%25B9%25E7%259B%25AE" target="_blank">​</a></h3> 
 <ul> 
  <li>*【Breaking】**使用 PReact 的项目需要额外安装<span> </span><code>@prefresh/webpack</code><span> </span>和<span> </span><code>@prefresh/babel-plugin</code>：</li> 
 </ul> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @prefresh/webpack @prefresh/babel-plugin --save-dev</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>2.4 使用 Vue2 的项目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%2324-%25E4%25BD%25BF%25E7%2594%25A8-vue2-%25E7%259A%2584%25E9%25A1%25B9%25E7%259B%25AE" target="_blank">​</a></h3> 
 <ul> 
  <li>*【Breaking】**使用 Vue2 的项目需要额外安装<span> </span><code>@vue/babel-preset-jsx</code>：</li> 
 </ul> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @vue/babel-preset-jsx --save-dev</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>2.5 使用 Vue3的项目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%2325-%25E4%25BD%25BF%25E7%2594%25A8-vue3%25E7%259A%2584%25E9%25A1%25B9%25E7%259B%25AE" target="_blank">​</a></h3> 
 <ul> 
  <li>*【Breaking】**使用 Vue3 的项目需要额外安装<span> </span><code>@vue/babel-plugin-jsx</code>：</li> 
 </ul> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @vue/babel-plugin-jsx --save-dev</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>3. 使用 Webpack5<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%233-%25E4%25BD%25BF%25E7%2594%25A8-webpack5" target="_blank">​</a></h3> 
 <p>开发者需要先卸载<span> </span><code>@tarojs/mini-runner</code><span> </span>和<span> </span><code>@tarojs/webpack-runner</code>：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> uninstall @tarojs/mini-runner @tarojs/webpack-runner</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>然后安装<span> </span><code>@tarojs/webpack5-runner</code>：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> </span><span style="color:#d73a49">install</span><span> @tarojs/webpack5-runner</span>
</span></code></pre> 
  </div> 
 </div> 
 <p>最后修改 Taro 编译配置即可：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><em>/** config/index.js */</em>
</span><span style="color:#393a34"><span style="color:#00009f">const</span><span> config </span><span style="color:#393a34">=</span><span> </span><span style="color:#393a34">&#123;</span>
</span><span style="color:#393a34"><span>  </span><span style="color:#36acaa">compiler</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">'webpack5'</span>
</span><span style="color:#393a34"><span style="color:#393a34">&#125;</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>4. 使用 React 18<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%234-%25E4%25BD%25BF%25E7%2594%25A8-react-18" target="_blank">​</a></h3> 
 <p>需要更新<span> </span><code>react</code>、<code>react-dom</code>、<code>@types/react</code><span> </span>的版本：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i react react-dom</span>
</span></code></pre> 
  </div> 
 </div> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#d73a49">npm</span><span> i @types/react --save-dev</span>
</span></code></pre> 
  </div> 
 </div> 
 <h3>5. 使用 pnpm<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%235-%25E4%25BD%25BF%25E7%2594%25A8-pnpm" target="_blank">​</a></h3> 
 <p>因为 pnpm 不允许<strong>幽灵依赖</strong>的存在，因此开发者需要在项目中手动安装下列依赖：</p> 
 <p><code>dependencies</code><span> </span>补充依赖：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/helper"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-weapp"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-alipay"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-tt"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-swan"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-jd"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/plugin-platform-qq"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/router"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/shared"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span><span style="color:#393a34"><span style="color:#36acaa">"@tarojs/taro-h5"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"3.5.0"</span><span style="color:#393a34">,</span>
</span></code></pre> 
  </div> 
 </div> 
 <p><code>devDependencies</code><span> </span>补充依赖：</p> 
 <p>安装项目对应的 Webpack 版本，如 Webpack5：</p> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#36acaa">"webpack"</span><span style="color:#393a34">:</span><span> </span><span style="color:#e3116c">"^5.73.0"</span>
</span></code></pre> 
  </div> 
 </div> 
 <h2>六、最后<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taro.zone%2Fblog%2F2022%2F07%2F26%2FTaro-3.5%23%25E5%2585%25AD%25E6%259C%2580%25E5%2590%258E" target="_blank">​</a></h2> 
 <p>下半年 Taro 团队的核心将围绕以下各方向展开：</p> 
 <ul> 
  <li>支持使用 Vite 进行编译（预计 Q3 推出 alpha 版本）</li> 
  <li>小程序方面将持续对性能进行优化、支持更多的 React/Vue 特性（如 Portal）和生态库（如 React/Vue Router）。</li> 
  <li>H5 方面将输出适配 Vue3 的 SSR 方案。</li> 
  <li>RN 方面将深入探索高阶功能，如地图、动画、2D及3D图形方案，并推出跨端可视化库，提升 Taro 跨端能力。</li> 
  <li>此外还会探索对于 Flutter 的适配。</li> 
 </ul> 
 <p>最后的最后，衷心感谢参与社区共建与交流的各位同学！上半年我们制定了开发者贡献制度，建立起规范的项目分工与有效的荣誉激励机制。未来 Taro 将积极探寻更中立与开放的开源治理机制，欢迎各位开发者参与到 Taro 社区的建设中~</p> 
 <p> </p> 
 <div style="margin-left:0px">
  本文作者：
 </div> 
 <div style="margin-left:0px">
  <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhiqingchen" target="_blank"><img alt="zhiqingchen" height="48" src="https://avatars1.githubusercontent.com/u/1876158?s=88&u=0305430cab9f7a516c720e7fc7f8680df1c835b9&v=4" width="48" referrerpolicy="no-referrer"></a> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhiqingchen" target="_blank">zhiqingchen</a>
  <span> </span>
  <span>58 同城前端架构师、Taro 技术委员会成员、Taro-RN 工作组 Owner</span>
 </div> 
 <div style="margin-left:0px">
  <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSyMind" target="_blank"><img alt="Cong-Cong Pan" height="48" src="https://avatars.githubusercontent.com/u/19852293?v=4" width="48" referrerpolicy="no-referrer"></a> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSyMind" target="_blank">Cong-Cong Pan</a>
  <span> </span>
  <span>Taro 合作者</span>
 </div> 
 <div style="margin-left:0px">
  <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAdvancedCat" target="_blank"><img alt="Flame" height="48" src="https://avatars.githubusercontent.com/u/7858761?v=4" width="48" referrerpolicy="no-referrer"></a> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAdvancedCat" target="_blank">Flame</a>
  <span> </span>
  <span>Taro 合作者</span>
 </div> 
 <div style="margin-left:0px">
  <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChen-jj" target="_blank"><img alt="JJ" height="48" src="https://storage.jd.com/cjj-pub-images/11807297.png" width="48" referrerpolicy="no-referrer"></a> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChen-jj" target="_blank">JJ</a>
  <span> </span>
  <span>Taro 技术委员会成员、Taro Core 工作组 Owner</span>
 </div> 
 <div style="margin-left:0px">
  <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZakaryCode" target="_blank"><img alt="TJ" height="48" src="https://avatars.githubusercontent.com/u/24262362?v=4" width="48" referrerpolicy="no-referrer"></a> </span>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FZakaryCode" target="_blank">TJ</a>
  <span> </span>
  <span>Taro 技术委员会成员、Taro Core 工作组</span>
 </div> 
 <p> </p> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            