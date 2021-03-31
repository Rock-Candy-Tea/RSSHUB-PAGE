
---
title: 'Calendar calendar控件的月份添加点击事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd5eebb3794d41f7b53ed7cf65d27fed~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd5eebb3794d41f7b53ed7cf65d27fed~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0"><a href="https://juejin.cn/post/6943478886063669278"></a>写在前面</h4>
<blockquote>
<p>elementui在使用日历也就是Calendar calendar控件的时候，发现它自带的上个月、今天、下个月是没有提供点击事件的，但是博主我做业务的时候用到了，因为排班的时候想要获取到上个月的信息需要给月份的信息，所以今天记录一下解决的办法！</p>
</blockquote>
<h4 data-id="heading-1"><a href="https://juejin.cn/post/6943478886063669278"></a>添加事件</h4>
<ul>
<li>在created的钩子函数中实现如下代码</li>
</ul>
<pre><code class="copyable">this.$nextTick(() => &#123;
        // 点击上个月
        let prevBtn = document.querySelector('.el-calendar__button-group .el-button-group>button:nth-child(1)');
        prevBtn.addEventListener('click', () => &#123;
          console.info(this.valueData)
         this.dateFormat('YYYY-mm-dd',this.valueData)
        &#125;)
        // 点击今天
        let currBtn = document.querySelector('.el-calendar__button-group .el-button-group>button:nth-child(2)');
        currBtn.addEventListener('click', () => &#123;
         console.info(this.valueData)
         this.dateFormat('YYYY-mm-dd',this.valueData)
        &#125;)
        // 点击下个月
        let nextBtn = document.querySelector('.el-calendar__button-group .el-button-group>button:nth-child(3)');
        nextBtn.addEventListener('click', () => &#123;
         console.info(this.valueData)
         this.dateFormat('YYYY-mm-dd',this.valueData)
        &#125;)
      &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2"><a href="https://juejin.cn/post/6943478886063669278"></a>时间格式化代码</h4>
<pre><code class="copyable">     /**
       * @param &#123;Object&#125; fmt 需要的时间格式 例如：'YYYY-mm-dd'
       * @param &#123;Object&#125; date  格林尼治时间 
       */
      dateFormat(fmt, date) &#123;
        let ret;
        const opt = &#123;
          "Y+": date.getFullYear().toString(), // 年
          "m+": (date.getMonth() + 1).toString(), // 月
          "d+": date.getDate().toString(), // 日
          "H+": date.getHours().toString(), // 时
          "M+": date.getMinutes().toString(), // 分
          "S+": date.getSeconds().toString() // 秒
        &#125;;
        for (let k in opt) &#123;
          ret = new RegExp("(" + k + ")").exec(fmt);
          if (ret) &#123;
            fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
          &#125;;
        &#125;;
        return fmt;
      &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3"><a href="https://juejin.cn/post/6943478886063669278"></a>打印结果<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd5eebb3794d41f7b53ed7cf65d27fed~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></h5>
<h4 data-id="heading-4"><a href="https://juejin.cn/post/6943478886063669278"></a>注意的点</h4>
<blockquote>
<p>valueData这个参数就是我们data中定义的，也就是需要我们在return中定义<strong>valueData: new Date()</strong> ,然后我们的Calendar calendar控件将其绑定才可以自动计算每个月份，代码如下：</p>
</blockquote>
<pre><code class="copyable"><el-calendar v-model='valueData' v-loading="loading" style="margin-top: 10px">
          <template slot="dateCell" slot-scope="&#123;date, data&#125;">
            <div class="currCalendarSty" @dblclick="calendarOnClick(data,date)">
              <p :class="data.isSelected ? 'is-selected' : ''">
                &#123;&#123; data.day.split('-').slice(1).join('-') &#125;&#125; &#123;&#123; data.isSelected ? '✔️' : ''&#125;&#125;
              </p>
              <el-row :gutter="20">
                <el-col :span="12" v-for="item in schdules[data.day]" :key="item.id" class="text item">
                  <div style="display: flex;flex-direction: column;justify-items: center;align-items: flex-start">
                    <div style="font-weight: bold">&#123;&#123;item.shifts !==null ? item.shifts.name : '未设置班次'&#125;&#125;</div>
                    <div>&#123;&#123;item.useralias&#125;&#125;
                      <el-tag v-if="item.user_status && item.user_status!==' '" size="mini" type="success">&#123;&#123;item.user_status&#125;&#125;</el-tag>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>
        </template>
 </el-calendar>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><a href="https://juejin.cn/post/6943478886063669278"></a>结束</h4>
<blockquote>
<p>具体每一个时间块上怎么显示，点击事件什么这里就不写了，第一是官方有，第二是自己也比较容易实现，这里需要说一个点，官方给的参数用好的话可以事半功倍，&#123; type, isSelected, day&#125;，type 表示该日期的所属月份，可选值有 prev-month，current-month，next-month；isSelected 标明该日期是否被选中；day 是格式化的日期，格式为 yyyy-MM-dd<br>
<a href="https://element.eleme.cn/#/zh-CN/component/calendar" target="_blank" rel="nofollow noopener noreferrer">组件地址</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            