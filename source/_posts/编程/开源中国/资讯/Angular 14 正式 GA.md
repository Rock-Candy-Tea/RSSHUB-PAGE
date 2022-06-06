
---
title: 'Angular 14 正式 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0604/090812_0TiT_2720166.gif'
author: 开源中国
comments: false
date: Sat, 04 Jun 2022 09:20:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0604/090812_0TiT_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Angular 14 已正式 GA。值得关注的新特性包括：</p> 
<ul> 
 <li>引入更加严格的类型化表单</li> 
 <li>Angular CLI 支持自动补全</li> 
 <li>独立组件发布开发者预览版</li> 
 <li>简化 page title 可访问性</li> 
 <li>Angular DevTools 支持离线使用，以及在 Firefox 中使用</li> 
 <li>引入实验性的 ESM 应用构建系统</li> 
 <li>……</li> 
</ul> 
<p><strong>独立组件</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fangular.io%2Fguide%2Fstandalone-components" target="_blank">Angular 独立组件</a>旨在通过减少对 NgModules 的需求来简化 Angular 应用程序的创作。在 v14 中，独立组件处于开发者预览版阶段。它们已准备好在应用程序中用于探索和开发，但目前不是稳定的 API，并且可能会在典型的向后兼容性模型之外发生变化。</p> 
<pre><code>import &#123; Component &#125; from '@angular/core';
import &#123; CommonModule &#125; from '@angular/common'; // includes NgIf and TitleCasePipe
import &#123; bootstrapApplication &#125; from '@angular/platform-browser';

import &#123; MatCardModule &#125; from '@angular/material/card';
import &#123; ImageComponent &#125; from './app/image.component';
import &#123; HighlightDirective &#125; from './app/highlight.directive';

@Component(&#123;
  selector: 'app-root',
  standalone: true,
  imports: [
    ImageComponent, HighlightDirective, // import standalone Components, Directives and Pipes
    CommonModule, MatCardModule // and NgModules
  ],
  template: `
    <mat-card *ngIf="url">
      <app-image-component [url]="url"></app-image-component>
      <h2 app-highlight>&#123;&#123;name | titlecase&#125;&#125;</h2>
    </mat-card>
  `
&#125;)
export class ExampleStandaloneComponent &#123;
  name = "emma";
  url = "www.emma.org/image";
&#125;

// Bootstrap a new Angular application using our `ExampleStandaloneComponent` as a root component.
bootstrapApplication(ExampleStandaloneComponent);</code></pre> 
<p>点此查看此特性的设计思路：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fdiscussions" target="_blank">https://github.com/angular/angular/discussions</a></p> 
<p><strong>更严格的类型化表单</strong></p> 
<p>Angular 14 <span style="background-color:#ffffff; color:#292929">为 A</span><span style="background-color:#ffffff; color:#292929">ngular Reactive Forms 包实现了更严格的类型。</span></p> 
<p><img height="451" src="https://static.oschina.net/uploads/space/2022/0604/090812_0TiT_2720166.gif" width="800" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fangular.io%2Fguide%2Ftyped-forms" target="_blank">类型化表单</a>确保表单控件、组和数组中的值在整个 API 中都是类型安全的——以实现更安全的表单，尤其是对于深度嵌套的复杂案例。</p> 
<pre><code class="language-javascript">const cat = new FormGroup(&#123;
   name: new FormGroup(&#123;
      first: new FormControl('Barb'),
      last: new FormControl('Smith'),
   &#125;),
   lives: new FormControl(9),
&#125;);

// Type-checking for forms values!
// TS Error: Property 'substring' does not exist on type 'number'.
let remainingLives = cat.value.lives.substring(1);

// Optional and required controls are enforced!
// TS Error: No overload matches this call.
cat.removeControl('lives');

// FormGroups are aware of their child controls.
// name.middle is never on cat
let catMiddleName = cat.get('name.middle');</code></pre> 
<p><strong>Angular CLI 支持自动补全</strong></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><span><span><span><span style="color:#292929"><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Angular v14 的新<code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fangular.io%2Fcli%2Fcompletion" target="_blank">ng completion</a></code>功能引入了实时预输入的自动补全功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#292929"><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为确保所有 Angular 开发者都知道这项特性，CLI 将提示开发者在 v14 中的第一个命令执行期间选择加入自动完成功能。开发者也可以手动运行<code>ng completion</code>，CLI 会自动进行设置。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><img src="https://static.oschina.net/uploads/space/2022/0604/091348_b5XS_2720166.gif" referrerpolicy="no-referrer"></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><strong>Angular DevTools 支持离线使用</strong></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start">Angular DevTools 调试扩展现已支持离线使用。对于 Firefox 用户，可在 Mozilla 附加组件中找到该扩展。</p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-89475e541d7c87ab537ecc5aa62602a8d2c.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><strong><span><span><span><span style="color:#292929"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>实验性 ESM 应用程序构建</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:-0.46em; margin-right:.86em; text-align:start"><span><span><span><span style="color:#292929"><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>最后，Angular v14 引入了一个实验性的基于 esbuild 的构建系统<code>ng build</code>，用于编译纯 ESM 输出。如需在</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#292929"><span><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>应用程序中尝试此操作，请更新浏览器构建器<code>angular.json</code>：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>"builder": "@angular-devkit/build-angular:browser"

"builder": "@angular-devkit/build-angular:browser-esbuild"</code></pre>
                                        </div>
                                      
</div>
            