
---
title: 'React 受控组件，Hooks 方式!'
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-22 03:42:50
thumbnail: 'https://segmentfault.com/img/bVcPcc9'
---

<div>   
<blockquote>作者：Shadeed<br>译者：前端小智<br>来源：dmitripavlutin</blockquote><blockquote><strong>点赞再看</strong>，微信搜索<strong>【<a href="https://mp.weixin.qq.com/s/sY9ufGGKfcdaAQ7KJQs3HA" rel="nofollow">大迁世界</a>】</strong>,B站关注<strong>【<a href="https://space.bilibili.com/31089477" rel="nofollow">前端小智</a>】</strong>这个没有大厂背景，但有着一股向上积极心态人。本文 <code>GitHub</code> <a href="https://github.com/qq449245884/xiaozhi" rel="nofollow">https://github.com/qq44924588...</a> 上已经收录，文章的已分类，也整理了很多我的文档，和教程资料。</blockquote><p>最近开源了一个 Vue 组件，还不够完善，欢迎大家来一起完善它，也希望大家能给个 star 支持一下，谢谢各位了。</p><p><strong>github 地址：<a href="https://github.com/qq449245884/vue-okr-tree" rel="nofollow">https://github.com/qq44924588...</a></strong></p><p>React 提供了两种方法来访问<code>input</code>字段的值:使用受控或非受控组件。我更喜欢受控组件，因为我们可以通过组件的状态读取和设置<code>input</code>的值。</p><p>在这篇文章中，我们来看看如何使用React Hook 实现受控组件。</p><h3>1.受控组件</h3><p>假设我们有一个简单的文本字段，并且想访问其值：</p><pre><code>import &#123; useState &#125; from 'react';

function MyControlledInput(&#123; &#125;) &#123;
  const [ value, setValue ] = useState('');
  const onChange = (event) => &#123;
    setValue(event.target.value);
  &#125;
  
  return (
    <>
        <div>Input value: &#123;value&#125;</div>
        <input value=&#123;value&#125; onChange=&#123;onChange&#125; />
    </>
  )
&#125;</code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcPcc9" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>打开示例(<a href="https://codesandbox.io/s/controlled-component-uwf8n)%E5%B9%B6%E5%9C%A8%E8%BE%93%E5%85%A5%E6%A1%86%E4%B8%AD%E8%BE%93%E5%85%A5" rel="nofollow">https://codesandbox.io/s/cont...</a>。可以看到 <code>value</code> 变量包含<code>input</code>字段中的值，并且在每次输入新值时，它也会更新。</p><p><code>input</code>字段受到控制，因为 React 从状态<code><input value = &#123;value&#125; ... /></code>设置其值。 当用户在<code>input</code> 中输入内容时，<code>onChange</code>处理程序会使用从事件对象<code>event.target.value</code>访问的输入值来更新状态。</p><p><code>value</code>变量表示用户真实输入的值。每次需要访问用户在<code>input</code>字段中输入的值时，只需读取value状态变量。</p><p>受控组件方法可以帮助我们访问任何输入类型的值:常规文本输入、<code>textarea</code>、<code>select</code> 等。</p><h3>2. 受控组件中的3个步骤中</h3><p>设置受控组件需要3个步骤：</p><ol><li>定义保存<code>input</code>值的状态:<code>const [value, setValue] = useState(")</code>。</li><li>创建事件处理程序，该事件处理程序在值更改时更新状态：</li></ol><pre><code class="javascript">const onChange = event => setValue(event.target.value);</code></pre><p>3.为<code>input</code>字段分配状态值，并添加事件处理程序：<code><input type="text" value=&#123;value&#125; onChange=&#123;onChange&#125; /></code>。</p><h3>3. state 作为真实的数组源</h3><p>我们看一个更复杂的例子。 页面中有一组员工姓名列表。 我们需要添加一个 <code>input</code>字段，当用户在此字段中键入内容时，员工列表将按姓名进行过滤。</p><pre><code class="jsx">function FilteredEmployeesList(&#123; employees &#125;) &#123;
 const [query, setQuery] = useState('');  
 const onChange = event => setQuery(event.target.value);
  const filteredEmployees = employees.filter(name => &#123;
    return name.toLowerCase().includes(query.toLowerCase());
  &#125;);

  return (
    <div>
 <h2>Employees List</h2>
 <input 
        type="text" 
 value=&#123;query&#125;        onChange=&#123;onChange&#125;      />
 <div className="list">
 &#123;filteredEmployees.map(name => <div>&#123;name&#125;</div>)&#125;
 </div>
 </div>
  );
&#125;</code></pre><p>打开演示(<a href="https://codesandbox.io/s/gracious-dawn-29qi6?file=/src/App.js)" rel="nofollow">https://codesandbox.io/s/grac...</a>，可以自行试试。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcPcde" alt="image" title="image" referrerpolicy="no-referrer"></span></p><h3>对输入进行防抖</h3><p>在前面的实现中，只要在<code>input</code>中输入一个字符，就会立即过滤列表。这并不总是很方便，因为在输入查询时它会分散用户的注意力。</p><p>我们通过<code>debounce</code>来改善用户体验：在最后一次更改后，以400毫秒的延迟过滤列表。</p><pre><code class="jsx">import &#123; useDebouncedValue &#125; from './useDebouncedValue';
function FilteredEmployeesList(&#123; employees &#125;) &#123;
  const [query, setQuery] = useState('');
 const debouncedQuery = useDebouncedValue(query, 400);  
  const onChange = event => setQuery(event.target.value);

  const filteredEmployees = employees.filter(name => &#123;
 return name.toLowerCase().includes(debouncedQuery.toLowerCase());  &#125;);

  return (
    <div>
 <h2>Employees List</h2>
 <input 
        type="text" 
        value=&#123;query&#125; 
        onChange=&#123;onChange&#125;
      />
 <div className="list">
 &#123;filteredEmployees.map(name => <div>&#123;name&#125;</div>)&#125;
 </div>
 </div>
  );
&#125;</code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcPcdu" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>打开演示(<a href="https://codesandbox.io/s/affectionate-swartz-9yk2u?file=/src/App.js)" rel="nofollow">https://codesandbox.io/s/affe...</a>，然后在<code>input</code>中输放值进行查询。员工列表不会在你打字时进行过滤，而是在最近一次按下键400毫秒后进行过滤。</p><p>下面是<code>useDebouncedValue()</code>的实现</p><pre><code class="javascript">export function useDebouncedValue(value, wait) &#123;
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => &#123;
    const id = setTimeout(() => setDebouncedValue(value), wait);
    return () => clearTimeout(id);
  &#125;, [value]);

  return debouncedValue;
&#125;</code></pre><p>受控组件是访问React中<code>input</code>字段的值的一种方便的技术。它不使用引用，而是作为访问<code>input</code>值的单一真实源。</p><p>~ 完，我们小智，我要去刷碗了，下期再见~</p><hr><p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://www.fundebug.com/?utm_source=xiaozhi" rel="nofollow">Fundebug</a>。</strong></p><p>原文：<a href="https://dmitripavlutin.com/controlled-inputs-using-react-hooks/" rel="nofollow">https://dmitripavlutin.com/co...</a></p><h2>交流</h2><p>文章每周持续更新，可以微信搜索「 大迁世界 」第一时间阅读和催更（比博客早一到两篇哟），本文 GitHub <a href="https://github.com/qq449245884/xiaozhi" rel="nofollow">https://github.com/qq449245884/xiaozhi</a>  已经收录，整理了很多我的文档，欢迎Star和完善，大家面试可以参照考点复习，另外关注公众号，后台回复<strong>福利</strong>，即可看到福利，你懂的。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000020353567?w=800&h=400" alt title referrerpolicy="no-referrer"></span></p>  
</div>
            