
---
title: 'Hikyuu 1.2.3 发布，高性能量化交易研究框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e0358e6c7e07012729af9f08488e3ffe4b1.png'
author: 开源中国
comments: false
date: Mon, 07 Mar 2022 08:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e0358e6c7e07012729af9f08488e3ffe4b1.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p><strong style="color:#333333">Hikyuu 1.2.3 已发布，这是一款量化交易研究框架。该版本更新如下：</strong></p> 
  <div> 
   <ol> 
    <li> <p style="margin-left:0; margin-right:0">指标支持动态参数</p> 
     <blockquote> 
      <div> 
       <p style="margin-left:0; margin-right:0">在通道信等证券行情软件中，其技术指标中的窗口参数通常支持整数，也支持使用指标，如:</p> 
       <div style="margin-left:0; margin-right:0"> 
        <div style="margin-left:0; margin-right:0"> 
         <pre style="margin-left:0; margin-right:0">T1:=HHVBARS(H,120); &#123;120内的最高点距今天的天数&#125;
L120:=LLV(L,T1+1); &#123;120内的最高点至今，这个区间的最低点&#125;
</pre> 
        </div> 
       </div> 
       <p style="margin-left:0; margin-right:0">现在，在 Hikyuu 中，也可以使用指标作为参数:</p> 
       <div style="margin-left:0; margin-right:0"> 
        <div style="margin-left:0; margin-right:0"> 
         <pre style="margin-left:0; margin-right:0"><span>T1</span> <span style="color:#666666">=</span> <span>HHVBARS</span><span>(</span><span>H</span><span>,</span> <span style="color:#208050">120</span><span>)</span>
<span>L120</span> <span style="color:#666666">=</span> <span>LLV</span><span>(</span><span>L</span><span>,</span> <span>T1</span><span style="color:#666666">+</span><span style="color:#208050">1</span><span>)</span>
<span>L120</span><span style="color:#666666">.</span><span>set_context</span><span>(</span><span>k</span><span>)</span>
<span>L120</span><span style="color:#666666">.</span><span>plot</span><span>()</span>
</pre> 
        </div> 
       </div> 
       <div>
        <img alt height="321" src="https://oscimg.oschina.net/oscnet/up-e0358e6c7e07012729af9f08488e3ffe4b1.png" width="480" referrerpolicy="no-referrer">
       </div> 
       <p style="margin-left:0; margin-right:0"><strong>注意事项</strong></p> 
       <p style="margin-left:0; margin-right:0">由于无法区分 Indicator(ind) 形式时，ind 究竟是指标参数还是待计算的输出数据，此时如果希望 ind 作为参数，需要通过 IndParam 进行显示指定，如：EMA(IndParam(ind))。</p> 
       <p style="margin-left:0; margin-right:0">最佳的的方式，则是通过指定参数名，来明确说明使用的是参数:</p> 
       <div style="margin-left:0; margin-right:0"> 
        <div style="margin-left:0; margin-right:0"> 
         <pre style="margin-left:0; margin-right:0"><span>x</span> <span style="color:#666666">=</span> <span>EMA</span><span>(</span><span>c</span><span>)</span>  <em># 以收盘价作为计算的输入</em>
<span>y</span> <span style="color:#666666">=</span> <span>EMA</span><span>(</span><span>IndParam</span><span>(</span><span>c</span><span>))</span> <em># 以收盘价作为 n 参数</em>
<span>z</span> <span style="color:#666666">=</span> <span>EMA</span><span>(</span><span>n</span><span style="color:#666666">=</span><span>c</span><span>)</span> <em># 以收盘价作为参数 n</em>
</pre> 
        </div> 
       </div> 
      </div> 
     </blockquote> </li> 
    <li> <p style="margin-left:0; margin-right:0">完善 PF、AF、SE</p> 
     <blockquote> 
      <div> 
       <p style="margin-left:0; margin-right:0">现在可以正常使用资产组合。:</p> 
       <div style="margin-left:0; margin-right:0"> 
        <div style="margin-left:0; margin-right:0"> 
         <pre style="margin-left:0; margin-right:0"><em># 创建一个系统策略</em>
<span>my_mm</span> <span style="color:#666666">=</span> <span>MM_FixedCount</span><span>(</span><span style="color:#208050">100</span><span>)</span>
<span>my_sg</span> <span style="color:#666666">=</span> <span>my_sg</span> <span style="color:#666666">=</span> <span>SG_Flex</span><span>(</span><span>EMA</span><span>(</span><span>n</span><span style="color:#666666">=</span><span style="color:#208050">5</span><span>),</span> <span>slow_n</span><span style="color:#666666">=</span><span style="color:#208050">10</span><span>)</span>
<span>my_sys</span> <span style="color:#666666">=</span> <span>SYS_Simple</span><span>(</span><span>sg</span><span style="color:#666666">=</span><span>my_sg</span><span>,</span> <span>mm</span><span style="color:#666666">=</span><span>my_mm</span><span>)</span>

<em># 创建一个选择算法，用于在每日选定交易系统</em>
<em># 此处是固定选择器，即每日选出的都是指定的交易系统</em>
<span>my_se</span> <span style="color:#666666">=</span> <span>SE_Fixed</span><span>([</span><span>s</span> <strong style="color:#007020">for</strong> <span>s</span> <strong style="color:#007020">in</strong> <span>blocka</span> <strong style="color:#007020">if</strong> <span>s</span><span style="color:#666666">.</span><span>valid</span><span>],</span> <span>my_sys</span><span>)</span>

<em># 创建一个资产分配器，用于确定如何在选定的交易系统中进行资产分配</em>
<em># 此处创建的是一个等比例分配资产的分配器，即按相同比例在选出的系统中进行资金分配</em>
<span>my_af</span> <span style="color:#666666">=</span> <span>AF_EqualWeight</span><span>()</span>

<em># 创建资产组合</em>
<em># 创建一个从2001年1月1日开始的账户，初始资金200万元。这里由于使用的等比例分配器，意味着将账户剩余资金在所有选中的系统中平均分配，</em>
<em># 如果初始资金过小，将导致每个系统都没有充足的资金完成交易。</em>
<span>my_tm</span> <span style="color:#666666">=</span> <span>crtTM</span><span>(</span><span>Datetime</span><span>(</span><span style="color:#208050">200101010000</span><span>),</span> <span style="color:#208050">2000000</span><span>)</span>
<span>my_pf</span> <span style="color:#666666">=</span> <span>PF_Simple</span><span>(</span><span>tm</span><span style="color:#666666">=</span><span>my_tm</span><span>,</span> <span>af</span><span style="color:#666666">=</span><span>my_af</span><span>,</span> <span>se</span><span style="color:#666666">=</span><span>my_se</span><span>)</span>

<em># 运行投资组合</em>
<span>q</span> <span style="color:#666666">=</span> <span>Query</span><span>(</span><span style="color:#666666">-</span><span style="color:#208050">500</span><span>)</span>
<span style="color:#666666">%</span><span>time</span> <span>my_pf</span><span style="color:#666666">.</span><span>run</span><span>(</span><span>Query</span><span>(</span><span style="color:#666666">-</span><span style="color:#208050">500</span><span>))</span>

<span>x</span> <span style="color:#666666">=</span> <span>my_tm</span><span style="color:#666666">.</span><span>get_funds_curve</span><span>(</span><span>sm</span><span style="color:#666666">.</span><span>get_trading_calendar</span><span>(</span><span>q</span><span>))</span>
<span>PRICELIST</span><span>(</span><span>x</span><span>)</span><span style="color:#666666">.</span><span>plot</span><span>()</span>
</pre> 
        </div> 
       </div> 
       <div>
        <img alt height="388" src="https://oscimg.oschina.net/oscnet/up-ae123df70c4e5baae456b26776dc90d3850.png" width="480" referrerpolicy="no-referrer">
       </div> 
      </div> 
     </blockquote> </li> 
    <li> <p style="margin-left:0; margin-right:0">修复fedora 34编译找不到路径报错，waning 提示</p> </li> 
    <li> <p style="margin-left:0; margin-right:0">fixed mysql 升级脚本错误</p> </li> 
    <li> <p style="margin-left:0; margin-right:0">fixed 复权后计算的净收益不对，并在使用前复权数据进行回测时给出警告（前复权回测属于未来函数）</p> </li> 
   </ol> 
  </div> 
  <p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">Hikyuu 是一款基于 C++/Python 的高性能开源量化交易研究框架，用于策略分析及回测（目前用于国内股票市场）。与其他量化平台或回测软件相比，其独特性在于：将完整的策略分解为不同的组件，通过重用不同的方面策略，最大化的减轻编写策略的负担，如常见的止损和资金管理策略，只需要简单指定已有的止损或资金管理策略等，即可完成不同的策略组合；同时，可自由遍历所有股票，对策略效果进行综合的统计分析。如下面的示例，简单更好不同的资金管理策略。入门示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnbviewer.jupyter.org%2Fgithub%2Ffasiondog%2Fhikyuu%2Fblob%2Fmaster%2Fhikyuu%2Fexamples%2Fnotebook%2F000-Index.ipynb%3Fflush_cache%3DTrue" target="_blank">https://nbviewer.jupyter.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True</a></p> 
  <p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">更多信息，参见项目主页：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhikyuu.org%2F" target="_blank">https://hikyuu.org</a> or <span> </span><a href="http://fasiondog.gitee.io/hikyuu/">http://fasiondog.gitee.io/hikyuu</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            