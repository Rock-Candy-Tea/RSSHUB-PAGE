
---
title: 'React旺财记账-数据持久化与数据展示'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3408'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 01:58:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=3408'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">更优雅的更新与删除</h1>
<h2 data-id="heading-1">更新</h2>
<h3 data-id="heading-2">不优雅版</h3>
<pre><code class="copyable">const updateTag = (id: number, obj: &#123; name: string &#125;) => &#123;
    //获取要修改的tag的下标
    const index = findTagIndex(id);
    //深拷贝tags
    //vue可以直接在原数据上修改，但react不支持这项功能，因为它认为数据不可变
    const tagsClone = JSON.parse(JSON.stringify(tags))
    //把tagsClone的第index个删掉，换成&#123;id: id, name: obj.name&#125;
    tagsClone.splice(index, 1, &#123;id: id, name: obj.name&#125;)
    setTags(tagsClone)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">优雅版</h2>
<pre><code class="copyable">const updateTag = (id: number, obj: &#123; name: string &#125;) => &#123;
    setTags(tags.map(tag => tag.id === id ? &#123;id, name: obj.name&#125; : tag));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">删除</h2>
<h3 data-id="heading-5">不优雅版</h3>
<pre><code class="copyable">const deleteTag = (id: number) => &#123;
    //获取要删除的tag的下标
    const index = findTagIndex(id);
    //深拷贝tags
    //vue可以直接在原数据上修改，但react不支持这项功能，因为它认为数据不可变
    const tagsClone = JSON.parse(JSON.stringify(tags))
    //把tagsClone的第index个删掉
    tagsClone.splice(index, 1)
    setTags(tagsClone)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">优雅版</h2>
<pre><code class="copyable">const deleteTag = (id: number) => &#123;
    setTags(tags.filter(tag => tag.id !== id))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">增加编辑页面回退功能</h1>
<p>为了使icon可以点击，需要修改Icon组件，即自定义Icon需要继承SVG所有属性</p>
<p>问题在于，当使用 <code>...rest</code>时，如果rest里拥有className那就会覆盖原本的className，为了解决这个问题，需要添加组件</p>
<pre><code class="copyable">yarn add classnames
yarn add --dev @types/classnames
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：保持版本号一致</p>
</blockquote>
<p>更新后的Icon代码：</p>
<pre><code class="copyable">  
import React from 'react';
import cs from 'classnames';

let importAll = (requireContext: __WebpackModuleApi.RequireContext) => requireContext.keys().forEach(requireContext);
try &#123;importAll(require.context('icons', true, /\.svg$/));&#125; catch (error) &#123;console.log(error);&#125;

type Props = &#123;
  name?: string
&#125; & React.SVGAttributes<SVGElement>

const Icon = (props: Props) => &#123;
  const &#123;name, children, className, ...rest&#125; = props
  return (
    <svg className=&#123;cs('icon', className)&#125; &#123;...rest&#125;>
      &#123;props.name && <use xlinkHref=&#123;'#' + props.name&#125;/>&#125;
    </svg>
  );
&#125;;

export default Icon;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">解决createId刷新后id重置问题</h1>
<p>解决方法是记住最后一次的id值，下次直接从 <code>localStorage</code> 中读取</p>
<pre><code class="copyable">let id = parseInt(window.localStorage.getItem('idMax') || '0')
const createId = () => &#123;
    id += 1;
    window.localStorage.setItem('idMax', id.toString())
    return id;
&#125;

export &#123;createId&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">解决标签持久化问题</h1>
<h2 data-id="heading-10">自定义useUpdate</h2>
<p>页面第一次默认刷新后，当deps改变时进行fn()</p>
<pre><code class="copyable">import &#123;useEffect, useRef&#125; from "react";

const useUpdate = (fn: () => void, deps: any[]) => &#123;
    const count = useRef(0)
    useEffect(() => &#123;
        count.current += 1;
    &#125;)
    useEffect(() => &#123;
        if (count.current > 1) &#123;
            fn()
        &#125;
    &#125;, deps);//这里必须是不可变数据
&#125;
export &#123;useUpdate&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">读取localStorage并新增</h2>
<p>注意默认标签的使用方法，即当localStorage为空时设定默认标签</p>
<pre><code class="copyable">useEffect(() => &#123;
    let localTags = JSON.parse(window.localStorage.getItem('tags') || '[]')
    if (localTags.length === 0) &#123;
        localTags = [
            &#123;id: createId(), name: '衣'&#125;,
            &#123;id: createId(), name: '食'&#125;,
            &#123;id: createId(), name: '住'&#125;,
            &#123;id: createId(), name: '行'&#125;
        ]
    &#125;
    setTags(localTags)
&#125;, [])
useUpdate(() => &#123;
    window.localStorage.setItem('tags', JSON.stringify(tags))
&#125;, [tags])//组件挂载时执行
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">解决记账页面持久化问题</h1>
<p>之前没有写点击ok后会发生什么，现在进行补充。在点击ok后，数据应该被存入localStorage中，即进行submit操作</p>
<pre><code class="copyable">const submit = () => &#123;
    addRecord(selected)
    alert('保存成功')
    setSelected(defaultFormdata)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中addRecord是自定义hook中的功能</p>
<pre><code class="copyable">import &#123;useEffect, useState&#125; from "react";
import &#123;useUpdate&#125; from "./useUpdate";

type newRecordItem = &#123;
    tagIds: number[]
    note: string
    category: '+' | '-'
    amount: number
&#125;

type RecordItem = newRecordItem & &#123;
    createdAt: string//格式为ISO 8601
&#125;


const useRecords = () => &#123;
    const [records, setRecords] = useState<RecordItem[]>([]);
    useEffect(() => &#123;
        setRecords(JSON.parse(window.localStorage.getItem('records') || '[]'))
    &#125;, [])
    useUpdate(() => &#123;
        window.localStorage.setItem('records', JSON.stringify(records))
    &#125;, [records])
    const addRecord = (newRecord: newRecordItem) => &#123;
        const record = &#123;...newRecord, createdAt: (new Date()).toISOString()&#125;
        setRecords([...records, record])
    &#125;
    return &#123;records, addRecord,&#125;
&#125;

export &#123;useRecords&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>小技巧：如果两种类型很像，想不重复代码，第一种方法是上面代码使用的 <code>&</code> 技巧，还可以把多的类型中的某几个删除，代码为<code>type newRecordItem = Omit<RecordItem, 'createdAt' | 'updatedAt'></code></p>
</blockquote></div>  
</div>
            