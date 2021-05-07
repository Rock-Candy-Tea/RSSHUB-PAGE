
---
title: 'typescript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6674296e867f4eb38918e202a4a67314~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 02:23:14 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6674296e867f4eb38918e202a4a67314~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>TypeScript 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集，而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。</p>
<p>TypeScript 提供最新的和不断发展的 JavaScript 特性，包括那些来自 2015 年的 ECMAScript 和未来的提案中的特性，比如异步功能和 Decorators，以帮助建立健壮的组件。</p>
<h3 data-id="heading-0">如何在 window 对象上显式设置属性</h3>
<p>对于使用过 <code>JavaScript</code> 的开发者来说，对于 <code>window.MyNamespace = window.MyNamespace || &#123;&#125;;</code> 这行代码并不会陌生。为了避免开发过程中出现冲突，我们一般会为某些功能设置独立的命名空间。</p>
<p>然而，在 TS 中对于 <code>window.MyNamespace = window.MyNamespace || &#123;&#125;;</code> 这行代码，TS 编译器会提示以下异常信息：</p>
<pre><code class="copyable">Property 'MyNamespace' does not exist on type 'Window & typeof globalThis'.(2339)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上异常信息是说在 <code>Window & typeof globalThis</code> 交叉类型上不存在 <code>MyNamespace</code> 属性。那么如何解决这个问题呢？最简单的方式就是使用类型断言：</p>
<pre><code class="copyable">(window as any).MyNamespace = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然使用 <code>any</code> 大法可以解决上述问题，但更好的方式是扩展 <code>lib.dom.d.ts</code> 文件中的 <code>Window</code> 接口来解决上述问题，具体方式如下：</p>
<pre><code class="copyable">declare interface Window &#123;
  MyNamespace: any;
&#125;

window.MyNamespace = window.MyNamespace || &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面我们再来看一下 <code>lib.dom.d.ts</code> 文件中声明的 <code>Window</code> 接口：</p>
<pre><code class="copyable">/**
 * A window containing a DOM document; the document property 
 * points to the DOM document loaded in that window. 
 */
interface Window extends EventTarget, AnimationFrameProvider, GlobalEventHandlers, 
  WindowEventHandlers, WindowLocalStorage, WindowOrWorkerGlobalScope, WindowSessionStorage &#123;
    // 已省略大部分内容
    readonly devicePixelRatio: number;
    readonly document: Document;
    readonly top: Window;
    readonly window: Window & typeof globalThis;
    addEventListener(type: string, listener: EventListenerOrEventListenerObject, 
      options?: boolean | AddEventListenerOptions): void;
    removeEventListener<K extends keyof WindowEventMap>(type: K, 
      listener: (this: Window, ev: WindowEventMap[K]) => any, 
      options?: boolean | EventListenerOptions): void;
    [index: number]: Window;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面我们声明了两个相同名称的 <code>Window</code> 接口，这时并不会造成冲突。<code>TypeScript</code> 会自动进行接口合并，即把双方的成员放到一个同名的接口中。</p>
<h3 data-id="heading-1">如何为对象动态分配属性</h3>
<p>在 <code>JavaScript</code> 中，我们可以很容易地为对象动态分配属性，比如：</p>
<pre><code class="copyable">let developer = &#123;&#125;;
developer.name = "semlinker";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码在 <code>JavaScript</code> 中可以正常运行，但在 <code>TypeScript</code> 中，编译器会提示以下异常信息：</p>
<pre><code class="copyable">Property 'name' does not exist on type '&#123;&#125;'.(2339)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>&#123;&#125;</code> 类型表示一个没有包含成员的对象，所以该类型没有包含 <code>name</code> 属性。为了解决这个问题，我们可以声明一个 <code>LooseObject</code> 类型：</p>
<pre><code class="copyable">interface LooseObject &#123;
  [key: string]: any
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该类型使用 索引签名 的形式描述 <code>LooseObject</code> 类型可以接受 <code>key</code> 类型是字符串，值的类型是 <code>any</code> 类型的字段。有了 <code>LooseObject</code> 类型之后，我们就可以通过以下方式来解决上述问题：</p>
<pre><code class="copyable">interface LooseObject &#123;
  [key: string]: any
&#125;

let developer: LooseObject = &#123;&#125;;
developer.name = "semlinker";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <code>LooseObject</code> 类型来说，它的约束是很宽松的。在一些应用场景中，我们除了希望能支持动态的属性之外，也希望能够声明一些必选和可选的属性。</p>
<p>比如对于一个表示开发者的 <code>Developer</code> 接口来说，我们希望它的 <code>name</code> 属性是必填，而 <code>age</code> 属性是可选的，此外还支持动态地设置字符串类型的属性。针对这个需求我们可以这样做：</p>
<pre><code class="copyable">interface Developer &#123;
  name: string;
  age?: number;
  [key: string]: any
&#125;

let developer: Developer = &#123; name: "semlinker" &#125;;
developer.age = 30;
developer.city = "XiaMen";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实除了使用 索引签名 之外，我们也可以使用 <code>TypeScript</code> 内置的工具类型 <code>Record</code> 来定义 <code>Developer</code> 接口：</p>
<pre><code class="copyable">// type Record<K extends string | number | symbol, T> = &#123; [P in K]: T; &#125;
interface Developer extends Record<string, any> &#123;
  name: string;
  age?: number;
&#125;

let developer: Developer = &#123; name: "semlinker" &#125;;
developer.age = 30;
developer.city = "XiaMen";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">如何理解泛型中的 <code><T></code></h3>
<p>对于刚接触 <code>TypeScript</code> 泛型的读者来说，首次看到<code><T></code> 语法会感到陌生。其实它没有什么特别，就像传递参数一样，我们传递了我们想要用于特定函数调用的类型。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6674296e867f4eb38918e202a4a67314~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考上面的图片，当我们调用 <code>identity<Number>(1)</code> ，<code>Number</code> 类型就像参数 1 一样，它将在出现 T 的任何位置填充该类型。图中 <code><T></code> 内部的 <code>T</code> 被称为类型变量，它是我们希望传递给 <code>identity</code> 函数的类型占位符，同时它被分配给 <code>value</code> 参数用来代替它的类型：此时 <code>T</code> 充当的是类型，而不是特定的 <code>Number</code> 类型。</p>
<p>其中 <code>T</code> 代表 <code>Type</code>，在定义泛型时通常用作第一个类型变量名称。但实际上 <code>T</code> 可以用任何有效名称代替。除了 <code>T</code> 之外，以下是常见泛型变量代表的意思：</p>
<ul>
<li>K（Key）：表示对象中的键类型；</li>
<li>V（Value）：表示对象中的值类型；</li>
<li>E（Element）：表示元素类型。</li>
</ul>
<p>其实并不是只能定义一个类型变量，我们可以引入希望定义的任何数量的类型变量。比如我们引入一个新的类型变量 U，用于扩展我们定义的 identity 函数：</p>
<pre><code class="copyable">function identity <T, U>(value: T, message: U) : T &#123;
  console.log(message);
  return value;
&#125;

console.log(identity<Number, string>(68, "Semlinker"));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9291edc6a2934e4397ea71160385f310~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了为类型变量显式设定值之外，一种更常见的做法是使编译器自动选择这些类型，从而使代码更简洁。我们可以完全省略尖括号，比如：</p>
<pre><code class="copyable">function identity <T, U>(value: T, message: U) : T &#123;
  console.log(message);
  return value;
&#125;

console.log(identity(68, "Semlinker"));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于上述代码，编译器足够聪明，能够知道我们的参数类型，并将它们赋值给 <code>T</code> 和 <code>U</code>，而不需要开发人员显式指定它们。</p>
<h3 data-id="heading-3">如何理解装饰器的作用</h3>
<p>在 <code>TypeScript</code> 中装饰器分为类装饰器、属性装饰器、方法装饰器和参数装饰器四大类。装饰器的本质是一个函数，通过装饰器我们可以方便地定义与对象相关的元数据。</p>
<p>比如在 <code>ionic-native</code> 项目中，它使用 <code>Plugin</code> 装饰器来定义 <code>IonicNative</code> 中 <code>Device</code> 插件的相关信息：</p>
<pre><code class="copyable">@Plugin(&#123;
  pluginName: 'Device',
  plugin: 'cordova-plugin-device',
  pluginRef: 'device',
  repo: 'https://github.com/apache/cordova-plugin-device',
  platforms: ['Android', 'Browser', 'iOS', 'macOS', 'Windows'],
&#125;)
@Injectable()
export class Device extends IonicNativePlugin &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中 <code>Plugin</code> 函数被称为装饰器工厂，调用该函数之后会返回类装饰器，用于装饰 <code>Device</code> 类。<code>Plugin</code> 工厂函数的定义如下：</p>
<pre><code class="copyable">// https://github.com/ionic-team/ionic-native/blob/v3.x/src/%40ionic-native/core/decorators.ts
export function Plugin(config: PluginConfig): ClassDecorator &#123;
  return function(cls: any) &#123;
    // 把config对象中属性，作为静态属性添加到cls类上
    for (let prop in config) &#123;
      cls[prop] = config[prop];
    &#125;

    cls['installed'] = function(printWarning?: boolean) &#123;
      return !!getPlugin(config.pluginRef);
    &#125;;
    // 省略其他内容
    return cls;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过观察 <code>Plugin</code> 工厂函数的方法签名，我们可以知道调用该函数之后会返回 <code>ClassDecorator</code> 类型的对象，其中 <code>ClassDecorator</code> 类型的声明如下所示：</p>
<pre><code class="copyable">declare type ClassDecorator = <TFunction extends Function>(target: TFunction) 
  => TFunction | void;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类装饰器顾名思义，就是用来装饰类的。它接收一个参数 —— <code>target</code>: <code>TFunction</code>，表示被装饰器的类。介绍完上述内容之后，我们来看另一个问题 <code>@Plugin(&#123;...&#125;)</code> 中的 <code>@</code> 符号有什么用？</p>
<p>其实 <code>@Plugin(&#123;...&#125;)</code> 中的 <code>@</code> 符号只是语法糖，为什么说是语法糖呢？这里我们来看一下编译生成的 <code>ES5</code> 代码：</p>
<pre><code class="copyable">var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) &#123;
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
&#125;;

var Device = /** @class */ (function (_super) &#123;
    __extends(Device, _super);
    function Device() &#123;
        return _super !== null && _super.apply(this, arguments) || this;
    &#125;
    Device = __decorate([
        Plugin(&#123;
            pluginName: 'Device',
            plugin: 'cordova-plugin-device',
            pluginRef: 'device',
            repo: 'https://github.com/apache/cordova-plugin-device',
            platforms: ['Android', 'Browser', 'iOS', 'macOS', 'Windows'],
        &#125;),
        Injectable()
    ], Device);
    return Device;
&#125;(IonicNativePlugin));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过生成的代码可知，<code>@Plugin(&#123;...&#125;)</code> 和 <code>@Injectable()</code> 最终会被转换成普通的方法调用，它们的调用结果最终会以数组的形式作为参数传递给 <code>__decorate</code> 函数，而在 <code>__decorate</code> 函数内部会以 <code>Device</code> 类作为参数调用各自的类型装饰器，从而扩展对应的功能。</p>
<p>此外，如果你有使用过 <code>Angular</code>，相信你对以下代码并不会陌生。</p>
<pre><code class="copyable">const API_URL = new InjectionToken('apiUrl');

@Injectable()
export class HttpService &#123;
  constructor(
    private httpClient: HttpClient,
    @Inject(API_URL) private apiUrl: string
  ) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>Injectable</code> 类装饰器修饰的 <code>HttpService</code> 类中，我们通过构造注入的方式注入了用于处理 <code>HTTP</code> 请求的 <code>HttpClient</code> 依赖对象。而通过 <code>Inject</code> 参数装饰器注入了 <code>API_URL</code> 对应的对象，这种方式我们称之为依赖注入<code>（Dependency Injection）</code>。</p>
<h3 data-id="heading-4">如何理解函数重载的作用</h3>
<p><strong>可爱又可恨的联合类型</strong></p>
<p>由于 <code>JavaScript</code> 是一个动态语言，我们通常会使用不同类型的参数来调用同一个函数，该函数会根据不同的参数而返回不同的类型的调用结果：</p>
<pre><code class="copyable">function add(x, y) &#123;
  return x + y;
&#125;

add(1, 2); // 3
add("1", "2"); //"12"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 <code>TypeScript</code> 是 <code>JavaScript</code> 的超集，因此以上的代码可以直接在 <code>TypeScript</code> 中使用，但当 <code>TypeScript</code> 编译器开启 <code>noImplicitAny</code> 的配置项时，以上代码会提示以下错误信息：</p>
<pre><code class="copyable">Parameter 'x' implicitly has an 'any' type.
Parameter 'y' implicitly has an 'any' type.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该信息告诉我们参数 <code>x</code> 和参数 <code>y</code> 隐式具有 <code>any</code> 类型。为了解决这个问题，我们可以为参数设置一个类型。因为我们希望 add 函数同时支持 <code>string</code> 和 <code>number</code> 类型，因此我们可以定义一个 <code>string | number</code> 联合类型，同时我们为该联合类型取个别名：</p>
<pre><code class="copyable">type Combinable = string | number;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在定义完 <code>Combinable</code> 联合类型后，我们来更新一下 <code>add</code> 函数：</p>
<pre><code class="copyable">
function add(a: Combinable, b: Combinable) &#123;
  if (typeof a === 'string' || typeof b === 'string') &#123;
    return a.toString() + b.toString();
  &#125;
  return a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为 <code>add</code> 函数的参数显式设置类型之后，之前错误的提示消息就消失了。那么此时的 <code>add</code> 函数就完美了么，我们来实际测试一下：</p>
<pre><code class="copyable">const result = add('semlinker', ' kakuqo');
result.split(' ');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面代码中，我们分别使用 <code>'semlinker'</code> 和 <code>'kakuqo'</code> 这两个字符串作为参数调用 <code>add</code> 函数，并把调用结果保存到一个名为 <code>result</code> 的变量上，这时候我们想当然的认为此时 <code>result</code> 的变量的类型为 <code>string</code>，所以我们就可以正常调用字符串对象上的 <code>split</code> 方法。但这时 <code>TypeScript</code> 编译器又出现以下错误信息了：</p>
<pre><code class="copyable">Property 'split' does not exist on type 'Combinable'.
Property 'split' does not exist on type 'number'.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显 <code>Combinable</code> 和 <code>number</code> 类型的对象上并不存在 <code>split</code> 属性。问题又来了，那如何解决呢？这时我们就可以利用 <code>TypeScript</code> 提供的函数重载。</p>
<p><strong>函数重载</strong></p>
<p>函数重载或方法重载是使用相同名称和不同参数数量或类型创建多个方法的一种能力。</p>
<pre><code class="copyable">function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: string, b: number): string;
function add(a: number, b: string): string;
function add(a: Combinable, b: Combinable) &#123;
  // type Combinable = string | number;
  if (typeof a === 'string' || typeof b === 'string') &#123;
    return a.toString() + b.toString();
  &#125;
  return a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们为 <code>add</code> 函数提供了多个函数类型定义，从而实现函数的重载。在 <code>TypeScript</code> 中除了可以重载普通函数之外，我们还可以重载类中的成员方法。</p>
<p>方法重载是指在同一个类中方法同名，参数不同（参数类型不同、参数个数不同或参数个数相同时参数的先后顺序不同），调用时根据实参的形式，选择与它匹配的方法执行操作的一种技术。所以类中成员方法满足重载的条件是：在同一个类中，方法名相同且参数列表不同。下面我们来举一个成员方法重载的例子：</p>
<pre><code class="copyable">class Calculator &#123;
  add(a: number, b: number): number;
  add(a: string, b: string): string;
  add(a: string, b: number): string;
  add(a: number, b: string): string;
  add(a: Combinable, b: Combinable) &#123;
  if (typeof a === 'string' || typeof b === 'string') &#123;
    return a.toString() + b.toString();
  &#125;
    return a + b;
  &#125;
&#125;

const calculator = new Calculator();
const result = calculator.add('Semlinker', ' Kakuqo');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，当 <code>TypeScript</code> 编译器处理函数重载时，它会查找重载列表，尝试使用第一个重载定义。如果匹配的话就使用这个。因此，在定义重载的时候，一定要把最精确的定义放在最前面。另外在 <code>Calculator</code> 类中，<code>add(a: Combinable, b: Combinable)&#123; &#125;</code> 并不是重载列表的一部分，因此对于 <code>add</code> 成员方法来说，我们只定义了四个重载方法。</p>
<h3 data-id="heading-5">interfaces 与 type 之间有什么区别</h3>
<ul>
<li>Objects/Functions</li>
</ul>
<p>接口和类型别名都可以用来描述对象的形状或函数签名：</p>
<p><strong>接口</strong></p>
<pre><code class="copyable">interface Point &#123;
  x: number;
  y: number;
&#125;

interface SetPoint &#123;
  (x: number, y: number): void;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>类型别名</strong></p>
<pre><code class="copyable">type Point = &#123;
  x: number;
  y: number;
&#125;;

type SetPoint = (x: number, y: number) => void;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Other Types</li>
</ul>
<p>与接口类型不一样，类型别名可以用于一些其他类型，比如原始类型、联合类型和元组：</p>
<pre><code class="copyable">// primitive
type Name = string;

// object
type PartialPointX = &#123; x: number; &#125;;
type PartialPointY = &#123; y: number; &#125;;

// union
type PartialPoint = PartialPointX | PartialPointY;

// tuple
type Data = [number, string];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Extend</li>
</ul>
<p>接口和类型别名都能够被扩展，但语法有所不同。此外，接口和类型别名不是互斥的。接口可以扩展类型别名，而反过来是不行的。</p>
<pre><code class="copyable">Interface extends interface

interface PartialPointX &#123; x: number; &#125;
interface Point extends PartialPointX &#123; 
  y: number; 
&#125;
Type alias extends type alias

type PartialPointX = &#123; x: number; &#125;;
type Point = PartialPointX & &#123; y: number; &#125;;
Interface extends type alias

type PartialPointX = &#123; x: number; &#125;;
interface Point extends PartialPointX &#123; y: number; &#125;
Type alias extends interface

interface PartialPointX &#123; x: number; &#125;
type Point = PartialPointX & &#123; y: number; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Implements</li>
</ul>
<p>类可以以相同的方式实现接口或类型别名，但类不能实现使用类型别名定义的联合类型：</p>
<pre><code class="copyable">interface Point &#123;
  x: number;
  y: number;
&#125;

class SomePoint implements Point &#123;
  x = 1;
  y = 2;
&#125;

type Point2 = &#123;
  x: number;
  y: number;
&#125;;

class SomePoint2 implements Point2 &#123;
  x = 1;
  y = 2;
&#125;

type PartialPoint = &#123; x: number; &#125; | &#123; y: number; &#125;;

// A class can only implement an object type or 
// intersection of object types with statically known members.
class SomePartialPoint implements PartialPoint &#123; // Error
  x = 1;
  y = 2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Declaration merging</li>
</ul>
<p>与类型别名不同，接口可以定义多次，会被自动合并为单个接口。</p>
<pre><code class="copyable">interface Point &#123; x: number; &#125;
interface Point &#123; y: number; &#125;

const point: Point = &#123; x: 1, y: 2 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            