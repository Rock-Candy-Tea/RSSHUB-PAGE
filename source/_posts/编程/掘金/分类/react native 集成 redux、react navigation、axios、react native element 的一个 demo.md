
---
title: 'react native 集成 redux、react navigation、axios、react native element 的一个 demo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1830'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 23:37:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=1830'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0"></h2>
<h2 data-id="heading-1">1. 前言：</h2>
<p>======</p>
<ul>
<li>react native 版本：0.64</li>
<li>redux： 官方推荐的全局数据管理的组件。保存的数据会在以下 2 个情况被销毁：APP 被杀死、手机重启。</li>
<li>react navigation： 官方推荐的路由及底部菜单栏实现</li>
<li>axios：官方推荐的一个 http 请求库</li>
<li>react native element：一个目前在 github 星星数量最多的一个 UI 库</li>
</ul>
<ol start="2">
<li>基础组件的安装及文档参考地址</li>
</ol>
<p>=================</p>
<h2 data-id="heading-2">2.1 React Native Elements</h2>
<ul>
<li>安装</li>
</ul>
<pre><code class="copyable">yarn add react-native-elements
yarn add react-native-vector-icons
npx react-native link react-native-vector-icons
yarn add react-native-safe-area-context
react-native link react-native-safe-area-context

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>参考<br>
<a href="https://reactnativeelements.com/docs/input" target="_blank" rel="nofollow noopener noreferrer">reactnativeelements.com/docs/input</a></li>
</ul>
<p><a href="https://react-native-elements.js.org/#/input" target="_blank" rel="nofollow noopener noreferrer">react-native-elements.js.org/#/input</a></p>
<h2 data-id="heading-3">2.2 路由及底部菜单栏 React Navigation</h2>
<ul>
<li>安装</li>
</ul>
<pre><code class="copyable">npm install @react-navigation/bottom-tabs

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>参考 <a href="https://reactnavigation.org/docs/tab-based-navigation" target="_blank" rel="nofollow noopener noreferrer">reactnavigation.org/docs/tab-ba…</a></li>
</ul>
<h2 data-id="heading-4">2.3 redux</h2>
<ul>
<li>参考 <a href="https://cn.redux.js.org/" target="_blank" rel="nofollow noopener noreferrer">cn.redux.js.org/</a></li>
</ul>
<h1 data-id="heading-5">关键文件</h1>
<h2 data-id="heading-6">app.js 入口文件</h2>
<ul>
<li>redux 全局 store 的绑定</li>
</ul>
<pre><code class="copyable">import 'react-native-gesture-handler'; // react navigation的必要配置
import * as React from 'react';
// import &#123; View &#125; from 'react-native';
import &#123;View&#125; from './src/components/Themed';
import Navigation from './src/navigator';
import &#123; Provider &#125; from 'react-redux';
import store from './src/redux/store';

const App = () => &#123;
  return (
    <View style=&#123;&#123; flex: 1 &#125;&#125;>
      <Provider store=&#123;store&#125;>
        <Navigation />
      </Provider>
    </View>
  );
&#125;;

export default App;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">页面路由、入口、跟随系统主题的配置</h2>
<ul>
<li>src\navigator\index.js</li>
</ul>
<pre><code class="copyable">/**
 * 页面路由、入口、跟随系统主题
 */
import * as React from 'react';
import &#123; useColorScheme &#125; from 'react-native';  //获取系统当前主题
import &#123; createStackNavigator &#125; from '@react-navigation/stack';
// 底部菜单栏主题参考： https://reactnavigation.org/docs/themes/#basic-usage
import &#123; DarkTheme, DefaultTheme, NavigationContainer &#125; from '@react-navigation/native';
import BTN from './bottomTabNavigator';
import LoginScreen from '../pages/login';
import DetailScreen from './detailScreen';
import SearchScreen from '../pages/common/search';
import &#123; ThemeProvider &#125; from 'react-native-elements';     //react native element 主题配置：参考https://reactnativeelements.com/docs/customization

//创建页面栈
const Stack = createStackNavigator();

function App() &#123;
  //获取系统配色
  const ColorScheme = useColorScheme();
  //修改底部菜单栏背景颜色为白色
  const lightTheme = &#123;
    ...DefaultTheme,
    colors: &#123;
      ...DefaultTheme.colors,
      background: '#fff'
    &#125;
  &#125;;
  return (
    <ThemeProvider useDark=&#123;ColorScheme === 'dark'&#125;>     
      <NavigationContainer theme=&#123;ColorScheme === 'dark' ? DarkTheme : lightTheme&#125;>
        <Stack.Navigator initialRoute>
          <Stack.Screen
            
            component=&#123;LoginScreen&#125;
            options=&#123;&#123; title: '登录', headerShown: false &#125;&#125;
          />
          <Stack.Screen
            
            component=&#123;BTN&#125;
            options=&#123;&#123; title: '首页', headerShown: false &#125;&#125;
          />

          <Stack.Screen  component=&#123;DetailScreen&#125; />

          &#123;/* 搜索页面 */&#125;
          <Stack.Screen  options=&#123;&#123; headerShown: false &#125;&#125; component=&#123;SearchScreen&#125; />
        </Stack.Navigator>
      </NavigationContainer>
    </ThemeProvider>
  );
&#125;

export default App;


<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">github 仓库地址</h1>
<p><a href="https://github.com/weijintao92/react-native-base.git" target="_blank" rel="nofollow noopener noreferrer">github.com/weijintao92…</a></p></div>  
</div>
            