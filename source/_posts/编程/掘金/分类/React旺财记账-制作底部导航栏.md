
---
title: 'React旺财记账-制作底部导航栏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fd15d8aaf6412ca8d8dc4c8b921da8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:41:17 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fd15d8aaf6412ca8d8dc4c8b921da8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一.下载icons</h1>
<p>进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iconfont.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iconfont.cn/" ref="nofollow noopener noreferrer">阿里巴巴矢量图标库</a>选择喜欢的icon下载。</p>
<h1 data-id="heading-1">二.自定义webpack配置 <code>yarn eject & svg-sprite-loader & Tree Shaking</code></h1>
<p>安装</p>
<pre><code class="copyable">yarn eject
yarn add --dev svg-sprite-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在config/webpack.config.js末尾的<code>return-module-rules-oneof</code>中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fd15d8aaf6412ca8d8dc4c8b921da8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
加入loader，注意官网options中的<code>...</code>要改为空</p>
<pre><code class="copyable">// webpack >= 2 multiple loaders
&#123;
    test: /.svg$/,
    use: [
        &#123;loader: 'svg-sprite-loader', options: &#123;&#125;&#125;,
        &#123;loader: 'svgo-loader', options: &#123;&#125;&#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续安装</p>
<pre><code class="copyable">yarn add --dev svgo-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入svg需要使用<code>require('icons/money.svg')</code>,防止treeshaking</p>
<h2 data-id="heading-2">现阶段Nav.tsx代码</h2>
<pre><code class="copyable">import styled from "styled-components";
import &#123;Link&#125; from "react-router-dom";
import React from "react";
require('icons/money.svg');
require('icons/tag.svg')
require('icons/statistic.svg')


const NavWrapper = styled.nav`
  line-height: 24px;
  box-shadow: 0 0 3px rgba(0, 0, 0, 0.25);

  > ul &#123;
    display: flex;

    > li &#123;
      width: 33.3333333%;
      padding: 4px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      .icon&#123;
        width: 24px;
        height: 24px;
      &#125;
    &#125;
  &#125;
`;

const Nav = () => &#123;
    return (
        <NavWrapper>
            <ul>
                <li>
                    <svg className="icon">
                        <use xlinkHref="#tag"/>
                    </svg>
                    <Link to="/tags">标签页</Link>
                </li>
                <li>
                    <svg className="icon">
                        <use xlinkHref="#money"/>
                    </svg>
                    <Link to="/money">记账页</Link>
                </li>
                <li>
                    <svg className="icon">
                        <use xlinkHref="#statistic"/>
                    </svg>
                    <Link to="/statistics">统计页</Link>
                </li>
            </ul>
        </NavWrapper>)
&#125;

export default Nav;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">万能排错</h3>
<p>如果出现 Cannot find module 问题，可以使用下面语句排错</p>
<pre><code class="copyable">yarn add @babel/helper-create-regexp-features-plugin
//安装这个模块即可
//或者使用万能排错
rm -rf node_modules
yarn install
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">icons代码优化：封装Icon & importAll & webpack-env</h2>
<pre><code class="copyable">import React from 'react';

let importAll = (requireContext: __WebpackModuleApi.RequireContext) => requireContext.keys().forEach(requireContext);
try &#123;importAll(require.context('icons', true, /\.svg$/));&#125; catch (error) &#123;console.log(error);&#125;

type Props = &#123;
  name: string
&#125;

//props需要声明类别
const Icon = (props: Props) => &#123;
  return (
    <svg className="icon">
      <use xlinkHref=&#123;'#' + props.name&#125;/>
    </svg>
  );
&#125;;

export default Icon;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时 <code>yarn add --dev @types/webpack-env@1.15.1</code> 防止 <code>__WebpackModuleApi</code> 报错</p>
<h2 data-id="heading-5">封装layout & 创建views</h2>
<pre><code class="copyable">import Nav from "./Nav";
import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  height: 100vh;
  display: flex;
  flex-direction: column;
`;

const Main = styled.div`
  flex-grow: 1;
  overflow: auto;
`;

const Layout = (props: any) => &#123;
    return (
        <Wrapper>
            <Main>
                &#123;props.children&#125;
            </Main>
            <Nav/>
        </Wrapper>
    )
&#125;

export default Layout;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2eedad2fd6dc49cfb89465b3e1e73129~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            