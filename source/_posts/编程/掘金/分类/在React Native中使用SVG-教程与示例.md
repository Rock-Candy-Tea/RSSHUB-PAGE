
---
title: '在React Native中使用SVG-教程与示例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e066e12d56465bbbff53dff80cec65~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 01:59:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e066e12d56465bbbff53dff80cec65~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当你在开发React Native应用程序时，你可能会被要求实现图标。现在，简单的方法是简单地提取图标的<code>.png</code> 或<code>.jpeg</code> 文件，并在React Native的<code>Image</code> 组件中使用它。这将为你带来好处，但你不会得到清晰的质量，而且你最终会用更高的图像文件大小来膨胀你的应用程序，这将增加你的应用程序捆绑大小。</p>
<p>你不应该在你的React Native应用中使用<code>.png</code> 或<code>.jpeg</code> 文件，而应该使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fsvg-vs-canvas%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/svg-vs-canvas/" ref="nofollow noopener noreferrer">SVG格式</a>。SVG是一种基于矢量的格式，可以无限扩展而不影响质量。</p>
<p>在本指南中，我们将演示如何使用<code>react-native-svg</code> 库在你的React Native应用中实现SVG图标。</p>
<p>我们将通过实际例子介绍以下内容。</p>
<ul>
<li><a href="https://juejin.cn/post/6993254126305951752#what-are-scalable-vector-graphics-svg" target="_blank" title="#what-are-scalable-vector-graphics-svg">什么是可扩展矢量图（SVG）？</a></li>
<li><a href="https://juejin.cn/post/6993254126305951752#does-react-native-support-svgs" target="_blank" title="#does-react-native-support-svgs">React Native是否支持SVG？</a></li>
<li><a href="https://juejin.cn/post/6993254126305951752#rendering-svg-shapes-in-react-native" target="_blank" title="#rendering-svg-shapes-in-react-native">在React Native中渲染SVG形状</a></li>
<li><a href="https://juejin.cn/post/6993254126305951752#how-to-render-svg-images-and-icons-in-react-native" target="_blank" title="#how-to-render-svg-images-and-icons-in-react-native">如何在React Native中渲染SVG图片和图标</a></li>
<li><a href="https://juejin.cn/post/6993254126305951752#rendering-svgs-using-xml-strings" target="_blank" title="#rendering-svgs-using-xml-strings">使用XML字符串渲染SVG</a></li>
</ul>
<h2 data-id="heading-0">什么是可扩展矢量图（SVG）？</h2>
<p>SVG是一种基于XML的格式，用于渲染矢量图像。矢量图像可以按照你的要求任意缩放而不出现像素化，因为矢量图像是由数学方程驱动的，不像其他图像格式那样有像素，比如<code>.png</code> 和<code>.jpeg</code> 。</p>
<p>由于SVG格式的矢量性质，图像与分辨率无关。SVG图像在任何屏幕上看起来都很清晰，从新的智能手机上华丽的285DPI像素密度屏幕到标准显示器的85DPI屏幕。与其他图像格式相比，SVG文件的尺寸也很小。</p>
<p>如果你在文本编辑器中打开一个SVG文件，你会看到一个带有数字和各种节点的大型XML代码。在本教程中，我们不会把重点放在SVG本身。相反，我们将演示如何在移动应用屏幕上渲染SVG。</p>
<h2 data-id="heading-1">React Native支持SVG吗？</h2>
<p>在移动应用中渲染SVG并不像在网络上那样简单，在网络上你可以直接使用SVG作为图片源，或者将SVG代码粘贴到你的HTML文件中。这是因为没有一个内置的React Native组件可以直接渲染SVG。</p>
<p>由于React Native没有提供对SVG的默认支持，我们必须从npm注册表中安装一些库。幸运的是，有一个流行的npm包，对于大多数的使用情况来说都很好用，叫做<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-native-svg%2Freact-native-svg" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-native-svg/react-native-svg" ref="nofollow noopener noreferrer">react-native-svg</a>。</p>
<p>让我们从建立一个React Native项目开始。运行下面的命令。</p>
<pre><code class="copyable">npx react-native init SvgDemoApp

<span class="copy-code-btn">复制代码</span></code></pre>
<p>要安装 react-native-svg 和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkristerkari%2Freact-native-svg-transformer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kristerkari/react-native-svg-transformer" ref="nofollow noopener noreferrer">react-native-svg-transformer</a>包，进入项目目录并运行以下命令。</p>
<pre><code class="copyable">cd SvgDemoApp
npm i react-native-svg
npm i --save-dev react-native-svg-transformer

<span class="copy-code-btn">复制代码</span></code></pre>
<p>react-native-svg为你在Android和iOS平台上的React Native项目提供SVG支持。 react-native-svg-transformer使你能够在React Native项目中导入本地SVG文件，就像你在网络上的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fgetting-started-with-create-react-app-d93147444a27%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/getting-started-with-create-react-app-d93147444a27/" ref="nofollow noopener noreferrer">Creact React App</a>项目那样。</p>
<p>如果你使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactnative.dev%2Fdocs%2Fenvironment-setup" target="_blank" rel="nofollow noopener noreferrer" title="https://reactnative.dev/docs/environment-setup" ref="nofollow noopener noreferrer">Expo CLI而不是React Native CLI</a>，你可以通过运行以下命令开始。</p>
<pre><code class="copyable">expo init SvgDemoApp
expo install react-native-svg

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">在React Native中渲染SVG形状</h2>
<p>让我们看看如何使用react-native-svg库来在你的应用程序中渲染SVG。</p>
<p>在你喜欢的编辑器中打开项目，从react-native-svg导入<code>Svg</code> 和<code>Circle</code> 组件，如下图所示。</p>
<pre><code class="copyable">import Svg, &#123; Circle &#125; from 'react-native-svg';

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><Svg></code> 组件是一个父级组件，需要它来渲染任何SVG形状。它就像是所有SVG形状的一个容器组件。如果你要渲染任何SVG形状，比如一个圆或一个多边形，你必须用它作为你的SVG组件的一个包装组件。</p>
<pre><code class="copyable"><Svg height="50%" width="50%" viewBox="0 0 100 100" >
       ...
</Svg>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><Svg></code> 组件需要三个道具：<code>height</code>,<code>width</code>, 和<code>viewBox</code> 。<code>viewBox</code> 道具描述了你的SVG在空间中的定位方式。<code>height</code> 和<code>width</code> 道具是不言自明的。</p>
<p>在<code><Svg></code> 组件内，渲染<code><Circle></code> 组件，如下所示。</p>
<pre><code class="copyable"><Svg height="50%" width="50%" viewBox="0 0 100 100" >
    <Circle cx="50" cy="50" r="50" stroke="purple" strokeWidth=".5" fill="violet" />
</Svg>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><Circle></code> 组件将<code>x</code> 和<code>y</code> 坐标分别作为<code>cx</code> 和<code>cy</code> 的道具。这些坐标定义了你的SVG组件在容器中的定位方式和位置。如果你要渲染一个不同的SVG形状，比如说一个矩形，同样会分别用<code>x</code> 和<code>y</code> props来表示。</p>
<p>为了描述圆的半径，你可以将一个整数作为字符串传递给<code>r</code> 道具。你可以设置这个值来增加或减少渲染的SVG圆的大小。</p>
<p><code>stroke</code> 道具可以用来表示SVG元素周围边框的颜色，<code>strokeWidth</code> 表示该边框的厚度。最后，<code>fill</code> 道具表示渲染的SVG元素的颜色。这些道具与本地HTML<code><svg></code> 元素上的属性相似，而且在大多数SVG组件中都是通用的。</p>
<p>请看一下在屏幕上渲染SVG圆圈的整个代码。</p>
<pre><code class="copyable">import React from 'react';
import &#123; StyleSheet, View &#125; from 'react-native';
import Svg, &#123; Circle &#125; from 'react-native-svg';

export default function App() &#123;
  return (
    <View style=&#123;styles.container&#125;>
      <Svg height="50%" width="50%" viewBox="0 0 100 100" >
        <Circle cx="50" cy="50" r="50" stroke="purple" strokeWidth=".5" fill="violet" />
      </Svg>
    </View>
  );
&#125;
const styles = StyleSheet.create(&#123;
  container: &#123;
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>你应该看到一个紫色的SVG圆，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e066e12d56465bbbff53dff80cec65~tplv-k3u1fbpfcp-watermark.image" alt="React Native SVG Circle Shape Example" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意，我把<code><Svg></code> 组件包裹在一个<code><View></code> 组件里面。你可以将你的SVG组件包裹在任何通用的容器组件内，比如<code><View></code> 或任何其他自定义的包裹组件。这样，你就可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fhow-to-build-a-basic-flexbox-layout-a-tutorial-with-examples%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/how-to-build-a-basic-flexbox-layout-a-tutorial-with-examples/" ref="nofollow noopener noreferrer">Flexbox布局</a>在屏幕上的任何地方放置和定位你的SVG组件，正如上面的例子所演示的那样。</p>
<p>同样，你也可以渲染其他SVG形状，如矩形、多边形、直线、椭圆等。</p>
<h2 data-id="heading-3">如何在React Native中渲染SVG图像和图标</h2>
<p>现在你已经了解了如何使用react-native-svg库渲染任何SVG，让我们探讨一下如何在你的应用程序中渲染SVG图标和图像。</p>
<p>在这里，你需要使用一个叫做<code>SvgUri</code> 的不同组件，所以让我们从库中导入它。</p>
<pre><code class="copyable">import &#123; SvgUri &#125; from 'react-native-svg';

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><SvgUri></code> 组件接受<code>width</code>,<code>height</code>, 和<code>uri</code> 道具。你可以指定<code>uri</code> prop指向SVG的URL。例如，如果你想渲染<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.w3.org%2FSVG%2Ftools%2Fsvgweb%2Fsamples%2Fsvg-files%2Fdebian.svg" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/debian.svg" ref="nofollow noopener noreferrer">这个</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.w3.org%2FSVG%2Ftools%2Fsvgweb%2Fsamples%2Fsvg-files%2Fdebian.svg" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/debian.svg" ref="nofollow noopener noreferrer">SVG</a>，你可以把这个URL分配给<code>uri</code> ，然后再分配给你的<code><SvgUri></code> 组件，如下图所示。</p>
<pre><code class="copyable"><SvgUri
    width="100%"
    height="100%"
    uri="https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/debian.svg"
/>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>src</code> 这与在React中渲染图片很相似，你可以指定<code><img></code> 的属性作为图片的URL。</p>
<p>上面的代码应该在屏幕上渲染SVG，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4dcfdcce42445ea08d521be6d49c5e~tplv-k3u1fbpfcp-watermark.image" alt="React Native SVG Icon Example" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><SvgUri></code> 你可以使用<code>width</code> 和<code>height</code> 组件的props来调整SVG的宽度和高度。与渲染SVG形状时不同，这里你不需要一个容器组件。</p>
<p>你可能会遇到需要引用本地SVG图标或项目内部的图像的情况。当你在设置示例项目时，记得你也安装了库<code>react-native-svg-transformer</code> 。你可以用它来渲染你项目中的本地SVG图标或图片。</p>
<p>首先，你需要对你的项目做一些配置上的改变。前往你的项目的<code>metro.config.js</code> 文件。如果这个文件在你的项目中不存在，你就需要创建它。</p>
<p>然后，在其中添加以下代码。</p>
<pre><code class="copyable">const &#123; getDefaultConfig &#125; = require('metro-config');

module.exports = (async () => &#123;
  const &#123;
    resolver: &#123; sourceExts, assetExts &#125;,
  &#125; = await getDefaultConfig();
  return &#123;
    transformer: &#123;
      babelTransformerPath: require.resolve('react-native-svg-transformer'),
    &#125;,
    resolver: &#123;
      assetExts: assetExts.filter(ext => ext !== 'svg'),
      sourceExts: [...sourceExts, 'svg'],
    &#125;,
  &#125;;
&#125;)();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，下载一个SVG并将其保存在你的项目中，类似于你下载一个你想在项目中使用的图片。假设你把你的SVG文件命名为<code>image.svg</code> 。现在你可以像其他组件一样导入这个SVG文件。</p>
<pre><code class="copyable">import SVGImg from './image.svg';

<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在任何组件中渲染它。</p>
<pre><code class="copyable"><SVGImg width=&#123;200&#125; height=&#123;200&#125; />

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码应该在屏幕上渲染相同的SVG。如果你的项目要求你在本地渲染SVG图标，你可以按照这个方法在你的应用程序中渲染不同的SVG图标。</p>
<h2 data-id="heading-4">使用XML字符串渲染SVG</h2>
<p>在少数情况下，如果你无法使用<code><SvgUri></code> 组件引用本地SVG，你可以使用XML字符串在React Native应用中渲染SVG。</p>
<p>假设你已经在你的项目中下载了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fthenewcode.com%2Fassets%2Fimages%2Fthumbnails%2Fhomer-simpson.svg" target="_blank" rel="nofollow noopener noreferrer" title="http://thenewcode.com/assets/images/thumbnails/homer-simpson.svg" ref="nofollow noopener noreferrer">这个SVG</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fthenewcode.com%2Fassets%2Fimages%2Fthumbnails%2Fhomer-simpson.svg" target="_blank" rel="nofollow noopener noreferrer" title="http://thenewcode.com/assets/images/thumbnails/homer-simpson.svg" ref="nofollow noopener noreferrer">文件</a>。如果你进入这个SVG文件内部，你会注意到一堆XML代码，其中有一个<code><svg></code> HTML元素。你可以使用<code><SvgXml></code> 组件从其XML代码中直接渲染一个SVG。</p>
<pre><code class="copyable">import &#123; SvgXml &#125; from 'react-native-svg';

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从SVG文件的XML代码中复制<code><svg></code> 元素内的所有内容，并将其存储在一个变量中。</p>
<pre><code class="copyable">const xml = `
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
width="500px" height="500px" viewBox="0 0 500 500" enable-background="new 0 0 500 500" xml:space="preserve">
...
</svg>
`;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，将上述变量传递给你的<code><SvgXml></code> 组件中的<code>xml</code> 道具，如下图所示。</p>
<pre><code class="copyable"><SvgXml xml=&#123;xml&#125; width="100%" height="100%" />

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以了!现在你应该在屏幕上看到上面的SVG了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7913aa7e26924b2ca7e380c16594670f~tplv-k3u1fbpfcp-watermark.image" alt="React Native SVG Homer Simpson Example" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">总结</h2>
<p>SVG对于渲染你想在React Native应用中使用的图片和图标来说是非常好的。你甚至可以用它们来创建复杂的形状和图案，为你的应用程序的设计增添更多的美感。</p>
<p>记住，在本地存储大量的SVG文件仍然会使你的应用程序变得臃肿。你应该始终避免在你的项目中保存大量的SVG文件并在本地引用它们。如果你绝对有必要，你可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjakearchibald.github.io%2Fsvgomg%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jakearchibald.github.io/svgomg/" ref="nofollow noopener noreferrer">这个方便的工具</a>来优化你的SVG文件。</p>
<p>我希望这个教程能让你更容易在你的React Native项目中使用SVG。你也可以探索和玩玩react<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-native-svg%2Freact-native-svg" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-native-svg/react-native-svg" ref="nofollow noopener noreferrer">-native-svg官方文档</a>中说明的例子。</p></div>  
</div>
            