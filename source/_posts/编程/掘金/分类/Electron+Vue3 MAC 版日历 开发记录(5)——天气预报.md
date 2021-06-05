
---
title: 'Electron+Vue3 MAC 版日历 开发记录(5)——天气预报'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 00:18:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了之前的框架整理和基本农历功能，接着就可以在 日历 View 里增加显示天气情况。</p>
<h2 data-id="heading-0">天气预报</h2>
<p>实现天气预报的功能，还是比较简单得。</p>
<ol>
<li>从天气预报服务商实时获取天气信息；</li>
<li>数据缓存；</li>
<li>显示在页面中；</li>
<li>设置是否显示天气预报的开关。</li>
</ol>
<h3 data-id="heading-1">和风天气</h3>
<p>在国内提供天气预报 API/SDK 的平台不少，其中「和风天气」是佼佼者。</p>
<blockquote>
<p>和风天气 API 为用户提供一个简洁的 RESTful API 接口，用以访问基于位置的天气数据</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d07ce3a8ef7247c8a4c46aa5abe0e3c1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发具体看：<a href="https://dev.qweather.com/" target="_blank" rel="nofollow noopener noreferrer">和风天气开发平台</a></p>
<h3 data-id="heading-2">服务端开发</h3>
<p>服务端主要使用到和风天气 API 的有：</p>
<ol>
<li>城市信息查询接口：<a href="https://dev.qweather.com/docs/api/geo/city-lookup/" target="_blank" rel="nofollow noopener noreferrer">dev.qweather.com/docs/api/ge…</a></li>
<li>实时天气接口：<a href="https://dev.qweather.com/docs/api/weather/weather-now/" target="_blank" rel="nofollow noopener noreferrer">dev.qweather.com/docs/api/we…</a></li>
<li>逐天(3 天)天气预报接口：<a href="https://dev.qweather.com/docs/api/weather/weather-daily-forecast/" target="_blank" rel="nofollow noopener noreferrer">dev.qweather.com/docs/api/we…</a></li>
<li>实时空气质量接口：<a href="https://dev.qweather.com/docs/api/air/air-now/" target="_blank" rel="nofollow noopener noreferrer">dev.qweather.com/docs/api/ai…</a></li>
</ol>
<p>具体 Laravel 代码：</p>
<pre><code class="copyable"><?php
/**
 * User: yemeishu
 */

namespace App\Http\Controllers;

use Carbon\Carbon;
use GuzzleHttp\Client;
use GuzzleHttp\Pool;
use Illuminate\Http\Request;
use GuzzleHttp\Psr7\Request as GRequest;
use Illuminate\Support\Arr;
use function Matrix\add;

class WeatherController extends Controller
&#123;
    private $counter = 1;
    private $result = [];
    private $public_id = "***";
    private $key = "***";

    // 和风天气开发平台
    // https://dev.qweather.com/docs/api/weather/
    // 实况接口
    private $now_finance_api = "https://api.qweather.com/v7/weather/now";
    private $now_dev_api = "https://devapi.qweather.com/v7/weather/now";

    // 3天预报接口
    private $td_finance_api = "https://api.qweather.com/v7/weather/3d";
    private $td_dev_api = "https://devapi.qweather.com/v7/weather/3d";

    // 空气质量接口
    private $air_finance_api = "https://api.qweather.com/v7/air/now";
    private $air_dev_api = "https://devapi.qweather.com/v7/air/now";

    // 城市信息搜索接口
    // 需要存于数据库，避免多次查询接口
    // 每天每个账号下所有应用前50000次免费
    private $city_lookup_api = "https://geoapi.qweather.com/v2/city/lookup";

    // 默认以石家庄经纬度为例
    private $coordinate_default = "114.48,38.03";

    private $location;

    private $finance_api = [
        "https://geoapi.qweather.com/v2/city/lookup",
        "https://api.qweather.com/v7/weather/now",
        "https://api.qweather.com/v7/weather/3d",
        "https://api.qweather.com/v7/air/now"
    ];

    private $dev_api = [
        "https://geoapi.qweather.com/v2/city/lookup",
        "https://devapi.qweather.com/v7/weather/now",
        "https://devapi.qweather.com/v7/weather/3d",
        "https://devapi.qweather.com/v7/air/now"
    ];

    public function weatherData(Request $request)
    &#123;
        $this->location = $request->input('location', $this->coordinate_default);

        $client = new Client();

        $requests = function ($apis) &#123;
            foreach ($apis as $api) &#123;
                yield new GRequest(
                    'GET',
                    "$api?location=$this->location&key=$this->key"
                );
            &#125;
        &#125;;

        $pool = new Pool(
            $client,
            $requests($this->dev_api),
            [
            'concurrency' => 3,
            'fulfilled' => function ($response, $index) &#123;
                $data = json_decode($response->getBody()->getContents(), true);
                $this->change2result($data);
                if ($this->countedAndCheckEnded($data)) &#123;
                    return $this->result;
                &#125;
            &#125;,
            'rejected' => function ($reason, $index) &#123;
                info('weather rejected', [$reason]);
                // this is delivered each failed request
            &#125;,
        ]);

        $promise = $pool->promise();

        $promise->wait();

        return $this->result;
    &#125;

    private function countedAndCheckEnded($data)
    &#123;
        if ($this->counter < count($this->dev_api))&#123;
            $this->counter++;
            return false;
        &#125;
        return true;
    &#125;

    private function change2result($data)
    &#123;
        if ($data['code'] == 200) &#123;
            if (Arr::has($data, 'updateTime')) &#123;
                $this->result['updateTime'] = (new Carbon($data['updateTime']))->toDateTimeString();
            &#125;

            if (Arr::has($data, 'now')) &#123;
                foreach ($data['now'] as $key => $value) &#123;
                    $this->result['weatherNow'][$key] = $value;
                &#125;
            &#125;

            if (Arr::has($data, 'daily')) &#123;
                $this->result['weatherDailies'] = $data['daily'];
            &#125;

            if (Arr::has($data, 'location')) &#123;
                $this->result['locations'] = $data['location'];
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认使用我自己所在地区的经纬度，接口返回数据如下：</p>
<pre><code class="copyable">&#123;
    locations: [
        &#123;
            name: "桥西",
            id: "101090120",
            lat: "38.02838135",
            lon: "114.46292877",
            adm2: "石家庄",
            adm1: "河北省",
            country: "中国",
            tz: "Asia/Shanghai",
            utcOffset: "+08:00",
            isDst: "0",
            type: "city",
            rank: "35",
            fxLink: "http://hfx.link/1toj1"
        &#125;
    ],
    updateTime: "2021-05-18 15:58:00",
    weatherNow: &#123;
        obsTime: "2021-05-18T15:53+08:00",
        temp: "30",
        feelsLike: "26",
        icon: "100",
        text: "晴",
        wind360: "135",
        windDir: "东南风",
        windScale: "5",
        windSpeed: "32",
        humidity: "33",
        precip: "0.0",
        pressure: "994",
        vis: "20",
        cloud: "10",
        dew: "10",
        pubTime: "2021-05-18T15:00+08:00",
        aqi: "79",
        level: "2",
        category: "良",
        primary: "O3",
        pm10: "56",
        pm2p5: "31",
        no2: "17",
        so2: "16",
        co: "0.9",
        o3: "183"
    &#125;,
    weatherDailies: [
        &#123;
            fxDate: "2021-05-18",
            sunrise: "05:10",
            sunset: "19:28",
            moonrise: "10:04",
            moonset: "01:00",
            moonPhase: "峨眉月",
            tempMax: "30",
            tempMin: "17",
            iconDay: "100",
            textDay: "晴",
            iconNight: "101",
            textNight: "多云",
            wind360Day: "180",
            windDirDay: "南风",
            windScaleDay: "3-4",
            windSpeedDay: "16",
            wind360Night: "0",
            windDirNight: "北风",
            windScaleNight: "1-2",
            windSpeedNight: "3",
            humidity: "34",
            precip: "0.0",
            pressure: "993",
            vis: "25",
            cloud: "0",
            uvIndex: "10"
        &#125;,
        &#123;
            fxDate: "2021-05-19",
            sunrise: "05:09",
            sunset: "19:28",
            moonrise: "11:08",
            moonset: "01:35",
            moonPhase: "峨眉月",
            tempMax: "30",
            tempMin: "18",
            iconDay: "302",
            textDay: "雷阵雨",
            iconNight: "350",
            textNight: "阵雨",
            wind360Day: "180",
            windDirDay: "南风",
            windScaleDay: "3-4",
            windSpeedDay: "16",
            wind360Night: "0",
            windDirNight: "北风",
            windScaleNight: "1-2",
            windSpeedNight: "3",
            humidity: "55",
            precip: "2.5",
            pressure: "991",
            vis: "24",
            cloud: "60",
            uvIndex: "5"
        &#125;,
        &#123;
            fxDate: "2021-05-20",
            sunrise: "05:08",
            sunset: "19:29",
            moonrise: "12:14",
            moonset: "02:06",
            moonPhase: "上弦月",
            tempMax: "28",
            tempMin: "18",
            iconDay: "101",
            textDay: "多云",
            iconNight: "150",
            textNight: "晴",
            wind360Day: "0",
            windDirDay: "北风",
            windScaleDay: "1-2",
            windSpeedDay: "3",
            wind360Night: "0",
            windDirNight: "北风",
            windScaleNight: "1-2",
            windSpeedNight: "3",
            humidity: "83",
            precip: "0.0",
            pressure: "994",
            vis: "24",
            cloud: "25",
            uvIndex: "11"
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上这些天气数据够我们当下使用了。</p>
<h3 data-id="heading-3">数据请求</h3>
<p>在本项目中，主要使用带有缓存功能的 <code>axios-cache-plugin</code>，同样的封装为 <code>WeatherService</code>：</p>
<pre><code class="copyable">'use strict';
import axios from 'axios';
import wrapper from 'axios-cache-plugin';
export default class WeatherService &#123;
  // 这里是使用 async/await
  async getWeathers(location: any) &#123;
    const locationStr = location.longitude + ',' + location.latitude;
    const http = wrapper(axios, &#123;
      maxCacheSize: 15,
      ttl: 7200000, //ms 数据缓存 2 小时
    &#125;);
    http.__addFilter(/weatherdata/);

    const res = await http(&#123;
      url: 'https://***.com/weatherdata',
      method: 'get',
      params: &#123;
        param: JSON.stringify(&#123;
          location: locationStr,
        &#125;),
      &#125;,
    &#125;);

    return res.data;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">显示到 View 中</h3>
<p>剩下的就比较简单了，就是怎么显示到 View 中了，还是在：</p>
<pre><code class="copyable">const dateWeather = this.showWeather(date, weather);
if (dateWeather == undefined) &#123;
  return &#123;
    html: `<div class="fc-daygrid-day-number">$&#123;dayNumberText&#125;</div>
        <div class="fc-daygrid-day-chinese">$&#123;dayTextInChinese&#125;</div>`,
  &#125;;
&#125; else &#123;
  const imgSrc = weathericons + '/../' + dateWeather.iconDay +'.png';
  return &#123;
    html: `<div class="fc-daygrid-day-number">$&#123;dayNumberText&#125;</div>
      <div class="fc-daygrid-day-chinese">$&#123;dayTextInChinese&#125;</div>
      <div class="fc-daygrid-dayweather">
        <img class="fc-daygrid-dayweather-iconday" src=$&#123;imgSrc&#125;/>
        <span class="fc-daygrid-dayweather-temp">$&#123;dateWeather.textDay&#125; $&#123;dateWeather.tempMin&#125;-$&#123;dateWeather.tempMax&#125;°C</span>
      </div>`,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为只显示 3 天的天气预报，所以还需要判断可否显示天气：</p>
<pre><code class="copyable">showWeather(date: Date, weather: any) &#123;

if (weather == null || weather.weatherDailies == null) &#123;
  return undefined;
&#125;
const dateString = Moment(date).format('YYYY-MM-DD');
const result = weather.weatherDailies.find((dateWeather: &#123; fxDate: string; &#125;) => dateWeather.fxDate == dateString);
return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来看看显示结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4856d33c2338447e9b8df8a47565cd2c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">小结</h2>
<p>关于开关控制是否显示天气的设置功能，下一步继续整理。</p>
<p>具体代码也放在 Github 上 <a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">fanly/fanlymenu</a>，欢迎查看！</p>
<p>最后感谢自己能坚持到第五天，也欢迎大家看看前四天的记录，对本项目有个初步的了解：</p>
<blockquote>
<p><a href="https://juejin.cn/post/6968670953836380196" target="_blank">Electron+Vue3 MAC 版日历开发记录(1)</a></p>
<p><a href="https://juejin.cn/post/6968972252389851172" target="_blank">Electron+Vue3 MAC 版日历开发记录(2)——功能清单</a></p>
<p><a href="https://juejin.cn/post/6969373297116971038" target="_blank">Electron+Vue3 MAC 版日历开发记录(3)——PrimeVue</a></p>
<p><a href="https://juejin.cn/post/6969743835253604388" target="_blank">Electron+Vue3 MAC 版日历 开发记录(4)——农历功能</a></p>
</blockquote></div>  
</div>
            