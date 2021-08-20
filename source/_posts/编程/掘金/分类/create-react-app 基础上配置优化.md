
---
title: 'create-react-app 基础上配置优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6998344140165480478'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 19:10:50 GMT
thumbnail: 'https://juejin.cn/post/6998344140165480478'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">版本详情：</h3>
<pre><code class="copyable">&#123;
  "name": "react-study",
  "version": "0.1.0",
  "private": true,
  "dependencies": &#123;
    "@babel/core": "7.12.3",
    "@pmmmwh/react-refresh-webpack-plugin": "0.4.3",
    "@svgr/webpack": "5.5.0",
    "@testing-library/jest-dom": "^5.14.1",
    "@testing-library/react": "^11.2.7",
    "@testing-library/user-event": "^12.8.3",
    "@typescript-eslint/eslint-plugin": "^4.5.0",
    "@typescript-eslint/parser": "^4.5.0",
    "antd": "^4.16.12",
    "axios": "^0.21.1",
    "babel-eslint": "^10.1.0",
    "babel-jest": "^26.6.0",
    "babel-loader": "8.1.0",
    "babel-plugin-named-asset-import": "^0.3.7",
    "babel-preset-react-app": "^10.0.0",
    "bfj": "^7.0.2",
    "camelcase": "^6.1.0",
    "case-sensitive-paths-webpack-plugin": "2.3.0",
    "classnames": "^2.3.1",
    "css-loader": "4.3.0",
    "dotenv": "8.2.0",
    "dotenv-expand": "5.1.0",
    "eslint": "^7.11.0",
    "eslint-config-react-app": "^6.0.0",
    "eslint-plugin-flowtype": "^5.2.0",
    "eslint-plugin-import": "^2.22.1",
    "eslint-plugin-jest": "^24.1.0",
    "eslint-plugin-jsx-a11y": "^6.3.1",
    "eslint-plugin-react": "^7.21.5",
    "eslint-plugin-react-hooks": "^4.2.0",
    "eslint-plugin-testing-library": "^3.9.2",
    "eslint-webpack-plugin": "^2.5.2",
    "file-loader": "6.1.1",
    "fs-extra": "^9.0.1",
    "html-webpack-plugin": "4.5.0",
    "identity-obj-proxy": "3.0.0",
    "jest": "26.6.0",
    "jest-circus": "26.6.0",
    "jest-resolve": "26.6.0",
    "jest-watch-typeahead": "0.6.1",
    "mini-css-extract-plugin": "0.11.3",
    "optimize-css-assets-webpack-plugin": "5.0.4",
    "pnp-webpack-plugin": "1.6.4",
    "postcss-flexbugs-fixes": "4.2.1",
    "postcss-loader": "3.0.0",
    "postcss-normalize": "8.0.1",
    "postcss-preset-env": "6.7.0",
    "postcss-safe-parser": "5.0.2",
    "prompts": "2.4.0",
    "react": "^17.0.2",
    "react-app-polyfill": "^2.0.0",
    "react-dev-utils": "^11.0.3",
    "react-dom": "^17.0.2",
    "react-refresh": "^0.8.3",
    "react-router-dom": "^5.2.0",
    "resolve": "1.18.1",
    "resolve-url-loader": "^3.1.2",
    "sass-loader": "^10.0.5",
    "semver": "7.3.2",
    "style-loader": "1.3.0",
    "terser-webpack-plugin": "4.2.3",
    "ts-pnp": "1.2.0",
    "url-loader": "4.1.1",
    "web-vitals": "^1.1.2",
    "webpack": "4.44.2",
    "webpack-dev-server": "3.11.1",
    "webpack-manifest-plugin": "2.2.0",
    "workbox-webpack-plugin": "5.1.4"
  &#125;,
  "scripts": &#123;
    "start": "node scripts/start.js",
    "build": "node scripts/build.js",
    "test": "node scripts/test.js"
  &#125;,
  "eslintConfig": &#123;
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  &#125;,
  "browserslist": &#123;
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  &#125;,
  "jest": &#123;
    "roots": [
      "<rootDir>/src"
    ],
    "collectCoverageFrom": [
      "src/**/*.&#123;js,jsx,ts,tsx&#125;",
      "!src/**/*.d.ts"
    ],
    "setupFiles": [
      "react-app-polyfill/jsdom"
    ],
    "setupFilesAfterEnv": [
      "<rootDir>/src/setupTests.js"
    ],
    "testMatch": [
      "<rootDir>/src/**/__tests__/**/*.&#123;js,jsx,ts,tsx&#125;",
      "<rootDir>/src/**/*.&#123;spec,test&#125;.&#123;js,jsx,ts,tsx&#125;"
    ],
    "testEnvironment": "jsdom",
    "testRunner": "D:\\react-study\\node_modules\\jest-circus\\runner.js",
    "transform": &#123;
      "^.+\\.(js|jsx|mjs|cjs|ts|tsx)$": "<rootDir>/config/jest/babelTransform.js",
      "^.+\\.css$": "<rootDir>/config/jest/cssTransform.js",
      "^(?!.*\\.(js|jsx|mjs|cjs|ts|tsx|css|json)$)": "<rootDir>/config/jest/fileTransform.js"
    &#125;,
    "transformIgnorePatterns": [
      "[/\\\\]node_modules[/\\\\].+\\.(js|jsx|mjs|cjs|ts|tsx)$",
      "^.+\\.module\\.(css|sass|scss)$"
    ],
    "modulePaths": [],
    "moduleNameMapper": &#123;
      "^react-native$": "react-native-web",
      "^.+\\.module\\.(css|sass|scss)$": "identity-obj-proxy"
    &#125;,
    "moduleFileExtensions": [
      "web.js",
      "js",
      "web.ts",
      "ts",
      "web.tsx",
      "tsx",
      "json",
      "web.jsx",
      "jsx",
      "node"
    ],
    "watchPlugins": [
      "jest-watch-typeahead/filename",
      "jest-watch-typeahead/testname"
    ],
    "resetMocks": true
  &#125;,
  "babel": &#123;
    "presets": [
      "react-app"
    ]
  &#125;,
  "devDependencies": &#123;
    "stylus": "^0.54.8",
    "stylus-loader": "^3.0.2"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行npm run eject将内置配置文件暴露出来</p>
<h3 data-id="heading-1">一、配置stylus </h3>
<p>TypeError: this.getOptions is not a function </p>
<p>原因：我的webpack版本是"webpack": "4.44.2",而版本不兼容导致stylus报错 <br>
改正为：npm i "stylus": "^0.54.8","stylus-loader": "^3.0.2"  </p>
<pre><code class="copyable">const stylusRegex = /\.styl$/;

const stylusModuleRegex = = /\.module\.styl$/;

//仿照sassRegex写一个json，改为stylusRegx

  &#123;
              test: stylusRegex,
              exclude: stylusModuleRegex,
              use: getStyleLoaders(
                &#123;
                  importLoaders: 3,
                  sourceMap: isEnvProduction
                    ? shouldUseSourceMap
                    : isEnvDevelopment,
                &#125;,
                'stylus-loader'
              ),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">二、配置 hash模式</h3>
<p>在eject出来的webpack.config.js文件中</p>
<pre><code class="copyable"> &#123;
              test: stylusRegex,
              use: getStyleLoaders(&#123;
                importLoaders: 3,
                sourceMap: isEnvProduction
                  ? shouldUseSourceMap
                  : isEnvDevelopment,
                modules:&#123;
                  getLocalIdent:getCSSModuleLocalIdent
                &#125;
              &#125;,
                'stylus-loader'
              ),
              sideEffects: true,

            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sideEffects：文件影响的副作用，可以为数组/boolean</p>
<p>找到</p>
<pre><code class="copyable"> modules:&#123;
                  getLocalIdent:getCSSModuleLocalIdent
                &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>中的getCSSModuleLocalIdent</p>
<p>路径为：</p>
<p><img alt src="https://juejin.cn/post/6998344140165480478" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img alt src="https://juejin.cn/post/6998344140165480478" loading="lazy" referrerpolicy="no-referrer"></p>
<p>找到并配置参数：</p>
<pre><code class="copyable">const className = loaderUtils.interpolateName(
    context,
    localName + '_' + hash,
    options
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hash为css样式后缀如图：</p>
<p><img alt src="https://juejin.cn/post/6998344140165480478" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就开启了css模块化，主要防止css重命名冲突</p>
<p>hash也可以为自定义随机数等。</p>
<h3 data-id="heading-3">三、优化classNames样式</h3>
<p>引入</p>
<pre><code class="copyable">npm install classnames
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在js中使用</p>
<pre><code class="copyable">import &#123;Component&#125; from 'react';
import styles from './styl.styl';
import classNames from "classnames/bind";

const ctx = classNames.bind(styles);

export default class Home extends Component &#123;
    constructor(props) &#123;
        super(props);
        this.state = &#123;
            flag: true,
        &#125;
    &#125;

    componentDidMount() &#123;
    &#125;

    render() &#123;
        const &#123;flag&#125; = this.state;
        return (
            <div className=&#123;ctx('page', flag?'p':'')&#125;>
                classNames
            </div>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在stylus中</p>
<pre><code class="copyable">.page
  width 400px
  height 400px
  color red
  background yellow

.p
  border-radius 40%
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前目录：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/752257c9fd2a483d8193d0e63bbc1619~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            