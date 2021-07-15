
---
title: 'Taro中曾遇到的那些天坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4371'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 23:09:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=4371'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当前项目组用的 版本是Taro v2.2.16</p>
<h2 data-id="heading-1">多层嵌套循环的数据解构时取值有问题</h2>
<h3 data-id="heading-2">栗子：</h3>
<pre><code class="copyable">import Taro from '@tarojs/taro';
import &#123; View &#125; from '@tarojs/components';
class A extends Taro.Component &#123;
  data = [
    &#123;
      title: '项目1',
      type: 1,
      children: [&#123; title: '项目1-1' &#125;, &#123; title: '项目1-2' &#125;],
    &#125;,
    &#123;
      title: '项目2',
      type: 2,
      children: [&#123; title: '项目2-1' &#125;, &#123; title: '项目2-2' &#125;],
    &#125;,
  ];
  render() &#123;
    return (
      <View>
        &#123;this.data.map((outItem) => &#123;
          const &#123; title, type, children &#125; = outItem;
          return (
            <View>
              <View>&#123;title&#125;</View>
              <View>
                &#123;children.map((innerItem) => &#123;
                  console.log(type); // 问题点所在，会打印出undefined
                  return (
                    <View>
                      &#123;type === 1 && <View>&#123;innerItem.title&#125; - 类型一</View>&#125;
                      &#123;type === 2 && (
                        <View>&#123;innerItem.title&#125; - 这是一个类型二</View>
                      )&#125;
                    </View>
                  );
                &#125;)&#125;
              </View>
            </View>
          );
        &#125;)&#125;
      </View>
    );
  &#125;
&#125;
export default A;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">现象：</h3>
<p>上面的console.log理应正常打印出type的值，但是Taro编译后，会打印出undefined。显而易见，下面的条件判断全部都会是false，从而出错。</p>
<ul>
<li>原因：</li>
</ul>
<p>查看编译后的代码发现，Taro会对map中的代码进行编译，编译结果大致如下</p>
<pre><code class="copyable">var loopArray128 = data.map(function (outItem) &#123;
  var outItem = &#123;
    $original: (0, _index.internal_get_original)(outItem)
  &#125;
  var _outItem$$original = outItem.$original,
      title = _outItem$$original.title,
      type = _outItem$$original.type,
      children = _outItem$$original.children;
  var $anonymousCallee__36 = children.map(function (innerItem) &#123;
    innerItem = &#123;
      $original: (0, _index.internal_get_original)(innerItem)
    &#125;;
    console.log(outItem.type); // 最后会编译成这样 outItem.type就不能取到想要的值了
    // ... other code 
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">解决方案：</h3>
<p>不要使用解构，以下是部分代码</p>
<pre><code class="copyable">render() &#123;
    return (
      <View>
        &#123;this.data.map((outItem) => &#123;
          const &#123; title, children &#125; = outItem;
          return (
            <View>
              <View>&#123;title&#125;</View>
              <View>
                &#123;children.map((innerItem) => &#123;
                  console.log(outItem.type); // 此时会编译成outItem.$original.type 值正常打印
                  return (
                    <View>
                      &#123;type === 1 && <View>&#123;innerItem.title&#125; - 类型一</View>&#125;
                      &#123;type === 2 && (
                        <View>&#123;innerItem.title&#125; - 这是一个类型二</View>
                      )&#125;
                    </View>
                  );
                &#125;)&#125;
              </View>
            </View>
          );
        &#125;)&#125;
      </View>
    );
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">props和state使用同样的变量名</h2>
<h3 data-id="heading-6">栗子：</h3>
<pre><code class="copyable">class Demo &#123;
  state = &#123;
    operationKeys: []
  &#125;
  
  render() &#123;
    const &#123; operationKeys &#125; = this.props
    console.log('operationKeys', operationKeys, operationKeys.length > 0)
    return (
      <View>
        &#123;operationKeys.length > 0 ? (
          <View>has data</View>
        ) : (
          <NoData/>
        )&#125;
      </View>
    )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">现象：</h3>
<p>组件在 props.operationKeys.length > 0 为true时，始终渲染</p>
<h3 data-id="heading-8">原因：</h3>
<p>Taro在编译 tsx(或jsx) 时，会将 js 逻辑和模板分离，js部分逻辑会根据 jsx 中的分支判断，生成一个 data，用于给模板进行渲染。jsx 中的标签部分会编译成wxml。如果props和state用了同样的变量名，并且state不更新，会导致渲染的时候一直使用state下的该变量，使得渲染错误。</p>
<h2 data-id="heading-9">JSX中三元表达式的嵌套也可能有问题（神奇的Taro）</h2>
<h3 data-id="heading-10">栗子：</h3>
<pre><code class="copyable">&#123;isSomething ? (
  <View className="row">
    <View className="row-title">栗子</View>
    <View className="row-content">
      &#123;Boolean(tampArrayList)
        ? tampArrayList.map((item, i) => (
        <View key=&#123;item.id + `$&#123;i&#125;`&#125;>
          &#123;`$&#123;item.name&#125;*$&#123;item.num&#125;，$&#123;item.content&#125;`&#125;
        </View>
      ))
      : '-'&#125;
    </View>
  </View>
) : null&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">现象：</h3>
<p>taro将代码编译的风马牛不相及，导致出现了不可预料的错误</p>
<pre><code class="copyable">// 编译给wxml用的变量
var anonymousState__temp5 = Boolean(tampArrayList);
// 这里不知道为什么省去了Boolean(tampArrayList)的表达式
// 导致tampArrayList.map报了Error
var loopArray197 = isWeddingPhoto ? tampArrayList.map(function (item, i) &#123;
  item = &#123;
    $original: (0, _index.internal_get_original)(item)
  &#125;;
  // 这里又神奇的出现了Boolean(tampArrayList)的表达式
  // $loopState__temp3为wxml使用的key值，根本与anyArrayList的状态无关
  var $loopState__temp3 = Boolean(anyArrayList) ? item.$original.id + ("" + i) : null;
  return &#123;
    $loopState__temp3: $loopState__temp3,
    $original: item.$original
  &#125;;
&#125;) : [];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">原因：</h3>
<p>Taro太辣鸡</p>
<h3 data-id="heading-13">解决：</h3>
<p>把里面的三元表达式赋值给一个变量</p>
<pre><code class="copyable">render() &#123;
  const productList = Boolean(tampArrayList)
    ? tampArrayList.map((item, i) => (
      <View key=&#123;item.id + `$&#123;i&#125;`&#125;>
        &#123;`$&#123;item.name&#125;*$&#123;item.num&#125;，$&#123;item.content&#125;`&#125;
      </View>
    ))
    : '-';
  // ...
  return (
    <View className="row-content">&#123;productList&#125;</View>
  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">还有一些 还没找到原因 但凭借踩坑经验 却顺利解决了的</h2>
<h3 data-id="heading-15">scroll-view使用flex布局,可能出现无效的情况（神奇的小程序）</h3>
<h3 data-id="heading-16">自定义组件内传入组件作为节点渲染出错</h3>
<h4 data-id="heading-17">栗子：</h4>
<pre><code class="copyable">import Taro from '@tarojs/taro';
import &#123; View, Input &#125; from '@tarojs/components';
// Cell是一个自定义组件，title是标题，renderContent传入DOM用于渲染内容
import &#123; Cell &#125; from '@components/index';
class A extends Taro.Component &#123;
  data = [
    &#123;
      title: '标题一',
      content: '输入的内容111',
    &#125;,
    &#123;
      title: '标题二',
      content: '输入的内容222',
    &#125;,
  ];
  render() &#123;
    return (
      <View>
        &#123;this.data.map((item) => &#123;
          const &#123; title, content &#125; = item;
          return (
            <Cell
              title=&#123;title&#125;
              renderContent=&#123;<Input placeholder="请输入" value=&#123;content&#125; />&#125;
            />
          );
        &#125;)&#125;
      </View>
    );
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">现象：</h4>
<p>Input的value值没有按照预想的显示出来。但content确有其值。</p>
<h4 data-id="heading-19">原因</h4>
<p>待确定</p>
<h4 data-id="heading-20">解决方案：</h4>
<p>只需要在最外层包裹一个View即可解决这个问题。</p>
<pre><code class="copyable"><Cell
  title=&#123;title&#125;
  renderContent=&#123;
    <View>
      <Input placeholder="请输入" value=&#123;content&#125; />
    </View>
  &#125;
 />

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">解构store中的方法后传入自定义组件编译报错</h3>
<pre><code class="copyable">import Taro from '@tarojs/taro';
import &#123; View, Input &#125; from '@tarojs/components';
// Cell是一个自定义组件，onClick是一个自定义的点击事件
import &#123; Cell &#125; from '@components/index';
// Store是用于存储数据的类（mobx）
import Store from './store';
class A extends Taro.Component &#123;
  store = new Store();
  
  render() &#123;
    const &#123; name, handleClick &#125; = this.store;
    return (
      <View>
        <View onClick=&#123;handleClick&#125;>&#123;name&#125;</View>
        <Cell onClick=&#123;handleClick&#125; />
      </View>
    );
  &#125;
&#125;
export default A;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">现象</h4>
<p>自定义组件Cell传入自定义方法之后，编译会出问题。但是View似乎就没有问题。</p>
<h4 data-id="heading-23">原因</h4>
<p>待确定</p>
<h4 data-id="heading-24">解决</h4>
<p>直接传入方法，或者使用匿名函数包裹。以下是部分代码：</p>
<pre><code class="copyable"><Cell onClick=&#123;() => handleClick()&#125; />
// or
<Cell onClick=&#123;this.store.handleClick&#125; />

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">总结</h2>
<ul>
<li>
<p>以上问题 有些Taro3中已经解决 但Taro 依旧有些坑，当我的迭代任务工作中百思不得其解的时候 就会在出问题的那个jsx 元素外层再包一层<code><View></code> 这是一个偷懒行为。但真的很管用</p>
</li>
<li>
<p>其次：遇到问题的时候可以先再去过一遍<a href="https://link.juejin.cn/?target=http%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Fbest-practice" target="_blank" rel="nofollow noopener noreferrer" title="http://taro-docs.jd.com/taro/docs/best-practice" ref="nofollow noopener noreferrer">Taro的最佳实践</a></p>
</li>
</ul>
<p><code>最后如果觉得本文有帮助 记得点赞三连哦 十分感谢</code></p></div>  
</div>
            