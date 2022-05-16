
---
title: 'Bootstrap 5.2.0 beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ddeeab301853fd72935ee81b4ebee653c5a.png'
author: 开源中国
comments: false
date: Mon, 16 May 2022 07:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ddeeab301853fd72935ee81b4ebee653c5a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Bootstrap v5.2.0-beta1 现已发布，这是自 v5 以来最大的一次发布更新。这个版本的特点是重新设计的文档、所有组件的 CSS 变量、响应式的 offcanvas、新的 helpers 和 utilities、<span style="background-color:#ffffff; color:#495057">改进的按钮和输入，以及许多底层改进。</span></p> 
<p>具体更新内容如下：</p> 
<h4><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>重新设计的文档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<p><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>开发团队重写了整个主页，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#212529">以更好地展示 Bootstrap 的所有功能。</span></p> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-ddeeab301853fd72935ee81b4ebee653c5a.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-a2ef317434030db7a00cb1e1d14135a9b25.png" width="500" referrerpolicy="no-referrer"></p> 
<p>变化包括简化了导航栏，取消了子导航，并更改了侧边栏以始终显示每个页面链接以提高可发现性。上面显示的也是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgetbootstrap.com%2Fdocs%2F5.2%2Fgetting-started%2Fintroduction%2F" target="_blank">更新后的快速入门指南</a>，它现在是通过 CDN 使用 Bootstrap 的分步指导指南。</p> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-6c71a41d063ef0c9787c5ebcd5da6e48a96.png" width="500" referrerpolicy="no-referrer"></p> 
<p>更新后的导航栏还有一个新版本选择器，适用于 v5.2.0 及更高版本。在任何页面上，单击版本并查看选项以导航到同一页面的先前次要版本。当一个页面不存在于旧版本时，你会在下拉列表中看到禁用的版本。官方表示，其目前没有计划跨主要版本链接页面。</p> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-2720df4f12177771b5d6c6b8c66f31d52f4.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#212529">文档搜索现在由最新版本的 Algolia DocSearch 提供支持，带来了改进的设计，甚至可以显示你最近的搜索。</span></p> 
<h4><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>设计调整</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<p style="text-align:start"><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为了配合文档的重新设计，开发团队给我们的按钮和输入法做了一些细化的边框半径值的更新。前后对比如下：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="149" src="https://oscimg.oschina.net/oscnet/up-686fa764554ba2ccfec9c526285b7037008.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start">以及 inputs 的前后对比：</p> 
<p style="text-align:start"><img alt height="355" src="https://oscimg.oschina.net/oscnet/up-ff939ca1a13539eaee8663c236bd02cde07.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>组件 CSS 变量</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<p style="text-align:start"><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在此版本中，所有的组件现在都包含 CSS 变量，以实现实时自定义、更轻松的主题化以及（很快）从 dark 模式开始的颜色模式支持。每个组件页面都已更新，包括相关 CSS 变量的参考指南。以 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgetbootstrap.com%2Fdocs%2F5.2%2Fcomponents%2Fbuttons%2F%23css" target="_blank">buttons</a> 为例：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<div> 
 <pre><code class="language-scss"><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-padding-x</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-padding-x</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-padding-y</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-padding-y</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-font-family</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-font-family</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0E)">@include</span><span style="color:var(--base07)"> rfs</span><span style="color:var(--base05)">(</span><span style="color:var(--base08)">$btn-font-size</span><span style="color:var(--base05)">,</span> <span style="color:var(--base05)">--</span><span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$prefix</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base08)">btn-font-size</span><span style="color:var(--base05)">);</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-font-weight</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-font-weight</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-line-height</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-line-height</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-color</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$body-color</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-bg</span><span style="color:var(--base05)">:</span> <span style="color:var(--base08)">transparent</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-border-width</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-border-width</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-border-color</span><span style="color:var(--base05)">:</span> <span style="color:var(--base08)">transparent</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-border-radius</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-border-radius</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-box-shadow</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-box-shadow</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-disabled-opacity</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-disabled-opacity</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base05)">;</span>
</span></span><span><span><span style="color:var(--base0A)">--#&#123;$prefix&#125;btn-focus-box-shadow</span><span style="color:var(--base05)">:</span> <span style="color:var(--base09)">0</span> <span style="color:var(--base09)">0</span> <span style="color:var(--base09)">0</span> <span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$btn-focus-width</span><span style="color:var(--base09)">&#125;</span> <span style="color:var(--base0B)">rgba</span><span style="color:var(--base05)">(</span><span style="color:var(--base0B)">var</span><span style="color:var(--base05)">(</span><span style="color:var(--base05)">--</span><span style="color:var(--base09)">#&#123;</span><span style="color:var(--base08)">$prefix</span><span style="color:var(--base09)">&#125;</span><span style="color:var(--base08)">btn-focus-shadow-rgb</span><span style="color:var(--base05)">)</span><span style="color:var(--base05)">,</span> <span style="color:var(--base09)">.5</span><span style="color:var(--base05)">);</span>
</span></span></code></pre> 
</div> 
<p style="color:#212529; text-align:start">几乎每个 CSS 变量的值都是通过 Sass 变量分配的，因此通过 CSS 和 Sass 进行自定义都得到了很好的支持。几个组件还包括通过 CSS 变量进行自定义的示例。</p> 
<p style="color:#212529; text-align:start"><img alt height="271" src="https://oscimg.oschina.net/oscnet/up-8210f18b8e2c903a6654ca0ea22a625fb77.png" width="500" referrerpolicy="no-referrer"></p> 
<h4><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的<code>_maps.scss</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<p style="text-align:start"><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bootstrap v5.2.0-beta1 引入了一个新的 Sass 文件<code>_maps.scss</code>，该文件从<code>_variables.scss</code>中提取了几个 Sass maps，以解决对 original map 的更新未应用于扩展它的 secondary maps 的问题。“这并不理想，但它解决了人们在使用自定义地图时长期存在的问题。”</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<div> 
 <pre><code class="language-diff"><span><span>// Functions come first
</span></span><span><span>  @import "functions";
</span></span><span><span>
</span></span><span><span>  // Optional variable overrides here
</span></span><span><span><span style="color:var(--bs-success)">+ $custom-color: #df711b;
</span></span></span><span><span><span style="color:var(--bs-success)">+ $custom-theme-colors: (
</span></span></span><span><span><span style="color:var(--bs-success)">+   "custom": $custom-color
</span></span></span><span><span><span style="color:var(--bs-success)">+ );
</span></span></span><span><span>
</span></span><span><span>  // Variables come next
</span></span><span><span>  @import "variables";
</span></span><span><span>
</span></span><span><span><span style="color:var(--bs-success)">+ // Optional Sass map overrides here
</span></span></span><span><span><span style="color:var(--bs-success)">+ $theme-colors: map-merge($theme-colors, $custom-theme-colors);
</span></span></span><span><span><span style="color:var(--bs-success)">+
</span></span></span><span><span><span style="color:var(--bs-success)">+ // Followed by our default maps
</span></span></span><span><span><span style="color:var(--bs-success)">+ @import "maps";
</span></span></span><span><span><span style="color:var(--bs-success)">+
</span></span></span><span><span>  // Rest of our imports
</span></span><span><span>  @import "mixins";
</span></span><span><span>  @import "utilities";
</span></span><span><span>  @import "root";
</span></span><span><span>  @import "reboot";
</span></span><span><span>  // etc
</span></span></code></pre> 
</div> 
<h4>New helpers and utilities</h4> 
<ul> 
 <li> <p><span>添加了新的<code>.text-bg-&#123;color&#125;</code>helpers。现在可以使用 .text-bg-* helpers 来设置具有对比前景色的背景色，而不是设置单独的 .text-* 和 .bg-* utilities。</span></p> </li> 
 <li> <p><span>扩展了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgetbootstrap.com%2Fdocs%2F5.2%2Futilities%2Ftext%2F%23font-weight-and-italics" target="_blank"><code>font-weight</code></a>utilities，包括用于 semibold fonts 的<code>.fw-semibold</code>。</span></p> </li> 
 <li> <p><span>扩展了 border-radius utilities ，包括两个新的尺寸：.rounded-4 和 .rounded-5，以提供更多选择。</span></p> </li> 
</ul> 
<h4>响应式 offcanvas</h4> 
<p>Offcanvas 组件现在有了响应式的变化。原始的 .offcanvas 类保持不变--它在所有视口都隐藏内容。要使其具有响应性，需将该 .offcanvas 类改为任何 .offcanvas-&#123;sm|md|lg|xl|xxl&#125; 类。</p> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.getbootstrap.com%2F2022%2F05%2F13%2Fbootstrap-5-2-0-beta%2F" target="_blank">查看官方博客</a>。</p>
                                        </div>
                                      
</div>
            