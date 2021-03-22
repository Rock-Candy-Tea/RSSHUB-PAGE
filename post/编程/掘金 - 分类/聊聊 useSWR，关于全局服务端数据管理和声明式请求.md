
---
title: 聊聊 useSWR，关于全局服务端数据管理和声明式请求
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 17:17:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c40d76f0bd8c400bb3bddfe3c988f173~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>前言</strong></p>
<p><a href="https://github.com/vercel/swr" target="_blank" rel="nofollow noopener noreferrer">useSWR</a> 是 Vercel 团队维护的 React 数据请求管理库，Vercel 同时也是 Next.js 的创始团队。有如此优秀的团队做支持，相信 useSWR 的思想和源码一定会给我们带来启发。</p>
</blockquote>
<p>在介绍 useSWR 之前，我们先看一个最简单的带有数据请求的 React 组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompWithFetch</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState()
  useEffect(<span class="hljs-function">() =></span> &#123;
    ;(<span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetchData()
        setData(data)
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        Message.error(<span class="hljs-string">"服务端错误"</span>)
        <span class="hljs-comment">// Hint: 优秀的代码，一定要 rethrow error，</span>
        <span class="hljs-comment">// 不要将错误吃掉</span>
        <span class="hljs-keyword">throw</span> err
      &#125;
    &#125;)()
  &#125;, [])

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;data&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果经常写这样的代码，那么肯定会想到自己封装一个 React Hook，该 Hook 以请求函数作为参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useFetch</span>(<span class="hljs-params">fetcher</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState()
  <span class="hljs-keyword">const</span> fetch = useCallback(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetcher()
      setData(data)
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      Message.error(<span class="hljs-string">"服务端错误"</span>)
      <span class="hljs-comment">// Hint: 优秀的代码，一定要 rethrow error，</span>
      <span class="hljs-comment">// 不要将错误吃掉</span>
      <span class="hljs-keyword">throw</span> err
    &#125;
  &#125;, [fetcher])

  <span class="hljs-comment">// fetcher 改变就再次获取数据</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    fetch()
  &#125;, [fetch])

  <span class="hljs-keyword">return</span> &#123;
    data,
    <span class="hljs-comment">// 暴露 fetch 给使用方，以便重新拉取数据</span>
    fetch,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再看看调用方代码，加深对 <code>useFetch</code> 的理解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompWithUseFetch</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [search, setSearch] = useState(<span class="hljs-string">""</span>)
  <span class="hljs-keyword">const</span> fetcher = useCallback(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 拼接 search 参数发起请求</span>
  &#125;, [search])

  <span class="hljs-keyword">const</span> &#123; data &#125; = useFetch(fetcher)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> setSearch(e.target.value)&#125; />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      &#123;data || "-"&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如 <code>useFetch</code> 所示，我们就完成了一个非常迷你的 useSWR 了。调用方需通过 useCallback 生成稳定的 fetcher 函数引用值，这点是为了在请求带有参数时，如果参数改变了就重新发起请求。暴露给调用方的 fetch 函数，可以应对主动刷新的场景，比如页面上的刷新按钮。</p>
<p>通过 <code>useFetch</code> 我们已经了解了 useSWR 的主要功能。接着我们进入正题吧，本文分为两个部分，第一部分介绍 useSWR 中的两大思想「全局服务端数据管理」和「声明式数据请求」，第二部分是使用 useSWR 后的总结，包括优缺点和最佳实践。</p>
<h1 data-id="heading-0">全局服务端数据管理</h1>
<p>useSWR 的 API 形式为 <code>useSWR(key, fetcher, config)</code>，它将 key 作为请求的 ID。如果多个组件需要共用一个请求，那它们就使用相同的 key 来调用 useSWR。useSWR 内部通过一个<a href="https://github.com/vercel/swr/blob/fa676db47512b07b539e8b933932d714a2e5d3b3/src/config.ts#L7" target="_blank" rel="nofollow noopener noreferrer">全局 Map</a> 来实现 key 和请求的关系，多次调用 useSWR 时，相同的 key 在 useSWR 中只存在一个请求结果。因此，再结合发布者订阅者模式，如果组件对某 key 对应的请求响应进行了修改，那么使用该 key 的其他组件都会收到最新的数据。这种天然的全局服务端数据管理方式，不仅保证了页面数据的一致性，而且可以非常简单地实现数据共享，这点将在<a href="https://juejin.cn/post/6942281123317678087#heading-8">“天然的全局状态方便多组件复用”</a>中被详细介绍。</p>
<h1 data-id="heading-1">声明式数据请求</h1>
<p>我们知道 React 是声明式 UI 库，开发者通过编写组件返回的 JSX 告诉 React 页面应该是什么样子的，然后 React 就会将页面更新为开发者想要的模样。因此开发者就只需关心如何写好 JSX 来描述页面，剩下的就交给 React 去优化吧。</p>
<p>useSWR 也是如此，它的 API 形式为 <code>useSWR(key, fetcher, config)</code>。如果我们只看前两个参数，我们通过 key 告诉 useSWR 我们需要什么请求，只要 key 改变了，我们便希望得到的是与 key 相对应的请求结果。这就是声明式数据请求，我们无需关心如何发起请求，<a href="https://juejin.cn/post/6942281123317678087#heading-7">请求的时序问题</a>，只需要告诉 useSWR 我们需要的请求即可。我们前面实现的 useFetch 也是声明式数据请求，useSWR 的 key 就可以理解为生成 fetcher 时 useCallback 的依赖。</p>
<p>useSWR 的参数 key 不仅可以是字符串，还可以是数组或函数。如果 key 是函数，则会将该函数的执行结果作为 key。如果 key 是数组，则会一次浅比较数组每项，如果有某项发生改变，则表示需要重新发起请求。</p>
<blockquote>
<p><strong>扩展知识</strong></p>
<p>useSWR 中 key 为数组时，数组中可以传对象，那 SWR 如何保证引用相等的对象所对应的 key 也相等呢？
参考<a href="https://github.com/vercel/swr/blob/fa676db47512b07b539e8b933932d714a2e5d3b3/src/libs/hash.ts#L33" target="_blank" rel="nofollow noopener noreferrer">源码</a>，useSWR 使用 WeakMap 将对象映射为整数。如果对象引用相等，则映射后的整数就一样，从而保证了 key 相等。</p>
</blockquote>
<h2 data-id="heading-2">条件请求</h2>
<p>通过 <code>key</code> 值，可以告诉 useSWR 我们需要的请求，那如何告诉 useSWR 不需要请求的场景呢？一般来说，程序中不需要什么，不调用就完了，但是 React Hook 不一样，它不能放在条件语句中，所以需要 useSWR 内置支持。</p>
<p>useSWR 通过 key 值是否为 null，来标识调用方是否需要请求。或者当 key 是一个函数时，函数执行时报错或返回 null 也可以。当不需要请求时，useSWR 的返回值始终是 <code>&#123; data: undefined, error: undefined, isValidating: false &#125;</code>。</p>
<h2 data-id="heading-3">如何命令式地触发数据请求</h2>
<p>如果页面上有一个刷新按钮，用户直接点击刷新按钮，期望重新获取服务端数据，通过 useSWR 如何实现该功能呢？</p>
<p>第一种方式是通过给 key 加一个计数器，每次点刷新按钮就让计数器加一，useSWR 便会获取新的数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [cnt, setCnt] = useState(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR([<span class="hljs-string">"/api/data"</span>, cnt], fetcher)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCnt(v => v + 1)&#125;>刷新<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>data: &#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这种方式有个缺点，它违背了 key 和请求之间的对应关系。如果后续还有组件要使用 /api/data 接口，这些新组件使用的 key 是 <code>'/api/data'</code>，就导致相同的请求对应着不同的 key。对 useSWR 而言，会认为它们是两个请求，便破坏了该请求的全局共享，导致页面数据不一致的结果。</p>
<p>第二种方式是通过命令式的方式发起请求。因为点刷新按钮时界面上所有的筛选参数都没有改变，所以传给 useSWR 的 key 就不会改变，那么声明式的数据请求方式就不会发起新的请求。useSWR 就考虑到这种场景，它返回的 <code>revalidate()</code> 方法，就是通过命令式方式重新发起请求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, revalidate &#125; = useSWR([<span class="hljs-string">"/api/data"</span>], fetcher)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> revalidate()&#125;>刷新<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>data: &#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">如何修改数据</h2>
<p>声明式的数据请求方式，只是告诉 useSWR 需要的请求，那我们有办法直接修改请求吗？</p>
<p>想想 React 是怎么做的呢？React 通过命令式的 setState() 来更新界面。所以 useSWR 也暴露了一个命令式的修改方式 <a href="https://useswr.vercel.app/docs/mutation" target="_blank" rel="nofollow noopener noreferrer"><code>mutate()</code></a>。</p>
<p>mutate 包括两个参数，第一个是新的数据（或是 Promise 对象），或者一个函数（函数调用实参是该请求的当前值）。第二个参数表示修改完成后是否应该重新发起请求，因为前端更新后的数据可能和后端的数据不一致，应以后端数据为准。</p>
<p>SWR 还提供了全局的 <code>mutate()</code> 方法，它的第一个参数是 key，表示想要修改的请求。<code>useSWR()</code> 返回的 <code>mutate()</code> 就是全局 mutate 方法绑定了 key 后的版本。</p>
<blockquote>
<p><strong>拓展知识</strong></p>
<p>在这方面，有个很专业的名词叫乐观更新（<a href="https://stackoverflow.com/questions/33009657/what-is-optimistic-updates-in-front-end-development" target="_blank" rel="nofollow noopener noreferrer">optimistic updates</a>），它是指用户通过页面修改服务端数据时，页面立即更新为用户修改后的数据，而不用等待服务端确认是否修改成功。这种方式有个弊端，那就是用户看到页面更新后就以为数据更新成功了，然后就把浏览器关了，如果服务端返回更新失败，也不能通知到用户了。因此最好能在乐观更新时，可以把请求的超时时间调小，或者在修改的内容旁展示加载态告知用户修改仍在进行中，提升用户体验。</p>
</blockquote>
<h1 data-id="heading-5">useSWR 的优势</h1>
<p>在介绍完 useSWR 的设计思想和基本使用后，接下来我们看看 useSWR 的优势，使用了它后解决了哪些问题。</p>
<h2 data-id="heading-6">1、实现了错误状态和加载状态</h2>
<p>useSWR 不仅和我们实现的 <code>useFetch</code> 一样好用，它的返回值还包括错误状态 error 和加载状态 isValidating。如果你曾经为每个请求都写过一次 <code>try catch</code> 和 <code>setLoading(true)</code>，那么用上 useSWR 后代码绝对会简洁不少。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用 useSWR 实现带有数据请求的 React 组件，和 useFetch 一样简洁。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompWithSWR</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, error, isValidating &#125; = useSWR(key, fetcher)

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了简洁之外，useSWR 还对 data/error/isValidating 做了优化，避免引起不必要的渲染。比如业务场景只关心请求的结果，当请求结果中数据不存在时，就在页面上展示占位符短横线。由于该场景并不关心加载状态和错误状态，那么 useSWR 就只会在 data 发生改变时才触发组件重新渲染。该优化通过 <code>Object.defineProperties</code> 实现依赖收集，可参考<a href="https://github.com/vercel/useSWR/blob/master/src/use-useSWR.ts#L753" target="_blank" rel="nofollow noopener noreferrer">源码</a>。</p>
<p>值得一提的是，当再次发起请求时，useSWR 会保留上次的请求结果，而不是重置 data 为 undefined。如果业务场景要求加载时重置 data/error，可在调用侧根据 isValidating 的值进行调整。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 发起请求时重置 data/error</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompWithSWR</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, error, isValidating &#125; = useSWR(key, fetcher)
  <span class="hljs-keyword">const</span> businessData = isValidating ? <span class="hljs-literal">undefined</span> : data
  <span class="hljs-keyword">const</span> businessError = isValidating ? <span class="hljs-literal">undefined</span> : data

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;businessData || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2. 解决了请求时序问题</h2>
<p>请求的时序问题是指用户操作页面两次，先后发出了请求 1 和请求 2，用户期望页面展示请求 2 的数据，但页面却展示了请求 1 的数据。</p>
<p><img alt="时序问题.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c40d76f0bd8c400bb3bddfe3c988f173~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为了保证程序的正确性，在搜索查询的页面和模块中，都需要解决时序问题。以往解决时序最简单的方法是使用一个递增的整数，每次请求结束都会用该整数判断当前请求是否是最后一个请求。如果是最后一个请求才使用它的响应结果，否则就忽略它。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 实现最简单的时序问题处理</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [search, setSearch] = useState(<span class="hljs-string">""</span>)
  <span class="hljs-keyword">const</span> [data, setData] = useState()

  <span class="hljs-keyword">const</span> fetcher = useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> reqCount = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">const</span> currCount = ++reqCount
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetchData(search)
        <span class="hljs-keyword">if</span> (currCount === reqCount) &#123;
          <span class="hljs-comment">// 如果是最后一次发起请求，才处理</span>
          setData(data)
        &#125;
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-keyword">if</span> (currCount === reqCount) &#123;
          <span class="hljs-comment">// 如果是最后一次发起请求，才处理</span>
          Message.error(<span class="hljs-string">"服务端错误"</span>)
          <span class="hljs-keyword">throw</span> err
        &#125;
      &#125;
    &#125;
  &#125;, [search])

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;fetcher&#125;</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      data: &#123;data || "-"&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 useSWR 后，我们就无需关心时序问题了，因为它的内部已经抽象了这块逻辑。</p>
<h2 data-id="heading-8">3. 天然的全局状态方便多组件复用</h2>
<p>如果只有一个组件会使用到某请求，我们一般都会将该请求的结果存在组件内部，这也符合软件设计内聚封装的思想。但如果多个组件需要共用该请求的数据，通常我们会将数据放到 Context 或 Redux 中。在实现该功能时，不仅要将数据移动到上层，还要调整「获取请求的代码」和「更新数据的代码」，繁琐且容易出错。</p>
<p>另一种解决办法是在需要该请求数据的多个组件中，都调用我们实现的 <code>useFetch</code> Hook。但是该方法有两个缺点。1.) 每个组件各自维护了一份数据，如果前端需要更新数据，那么两份数据如何同步就会变得很困难。2.) 每个组件都会发起一次请求，且不说对同一个请求发出多次会浪费资源，而且两次请求的结果也可能存在数据不一致的情况。由于这些缺点，所以还是使用上一种方案的全局数据管理更靠谱些。</p>
<p>useSWR 内部便是通过全局数据实现，如果调用 <code>useSWR(key, fetcher)</code> 的 key 一样，它们就会使用同一份数据。如果我们使用 useSWR 在组件 A 中使用了请求 <code>/api/data</code> 的数据，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在组件 A 中获取请求 `/api/data` 的数据</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR(<span class="hljs-string">"/api/data"</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
    <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall"</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件A：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后组件 B 也需要使用该请求。那么我们先复制一下代码看看效果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在组件 B 中也获取请求 `/api/data` 的数据</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR(<span class="hljs-string">"/api/data"</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
    <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall"</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件B：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可能会觉得这样的写法也要发出两次请求，但实际上只要 CompA 和 CompB 的挂载时间之差小于 <a href="https://useswr.vercel.app/zh-CN/docs/options" target="_blank" rel="nofollow noopener noreferrer">dedupingInterval（默认值是 2000ms）</a> ，useSWR 就只会发出一次请求。目前 useSWR 是在 <a href="https://github.com/vercel/swr/blob/fa676db47512b07b539e8b933932d714a2e5d3b3/src/use-swr.ts#L538" target="_blank" rel="nofollow noopener noreferrer">useLayoutEffect</a> 钩子回调中尝试发起请求的。</p>
<p>如果页面是同时展示组件 A 和组件 B，那么就不会发出两次请求，因为如果「执行组件 A 钩子回调」和「执行组件 B 钩子回调」之间时间超过 2s，那页面就太卡了，用户也该喷了。</p>
<p>如果页面先展示组件 A，用户点击按钮后才展示组件 B，组件 A 和 B 的挂载时间超过了 2s，那么组件 B 挂载时重新获取数据也是合理的，毕竟上次获取的请求数据可能已经是脏数据了（毕竟服务端随时都可能更新数据）。</p>
<p>当然也存在某些特殊场景，我们就是不想 B 重新发起请求，比如当数据更新后，就会导致组件 A 重新执行 Render 过程，进一步导致莫名其妙的 bug 或性能问题。这时可以给组件 B 传 <code>revalidateOnMount: false</code>，让组件 B 在挂载时不会发起请求。</p>
<p>接下来我们再简化下代码，将请求相关的公共代码提炼为函数 <code>useData</code>，然后在组件 A 和组件 B 中调用 <code>useData</code> 就完美了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useData</span>(<span class="hljs-params">revalidateOnMount</span>) </span>&#123;
  <span class="hljs-keyword">return</span> useSWR(
    <span class="hljs-string">"/api/data"</span>,
    <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
      <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall"</span>
    &#125;,
    &#123;
      revalidateOnMount,
    &#125;
  )
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useData()
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件A：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 根据需求，可以传参 false，来避免组件 B 在挂载时发起请求</span>
  <span class="hljs-keyword">const</span> &#123; data &#125; = useData()
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件B：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">4. 轻松实现数据预加载</h2>
<p>因为用户 Hover 到某按钮时，就极可能会点击该按钮，所以常见的数据预加载场景就是在用户 Hover 到某按钮时，预加载点击按钮后需要的数据，以便用户点击按钮后能立即看到结果，而不是看到“数据加载中...”，提升用户体验。</p>
<p>我们先梳理下实现数据预加载的方式有哪些？</p>
<ol>
<li>通过将数据提升，达到多组件复用来实现。</li>
<li>通过拿到后续组件的 ref 通过调用 <code>ref.prefetch()</code> 来实现。</li>
<li>通过接口缓存实现，比如将接口响应缓存 1s，1s 内发起点击就会立即使用缓存。</li>
<li>等等...</li>
</ol>
<p>前两种方式都伴随着不少的开发量。第三种方式简单，但容易失效，比如：用户 Hover 到按钮上等了 2s 在点击。</p>
<p>使用 useSWR 实现预加载的方式只需三步。</p>
<ol>
<li>给请求所在 Hook 增加 revalidateOnMount 参数。</li>
<li>在实现预加载的组件中，引用该 Hook 并传参 revalidateOnMount 为 false。</li>
<li>给按钮增加 onMouseEnter 事件处理函数，在函数中调用 revalidate()。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用 useSWR 实现预加载</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useData</span>(<span class="hljs-params">revalidateOnMount</span>) </span>&#123;
  <span class="hljs-keyword">return</span> useSWR(
    <span class="hljs-string">"/api/data"</span>,
    <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
      <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall"</span>
    &#125;,
    &#123;
      revalidateOnMount,
    &#125;
  )
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [visible, setVisible] = useState(<span class="hljs-literal">false</span>)
  <span class="hljs-keyword">const</span> &#123; revalidate &#125; = useData(<span class="hljs-literal">false</span>)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      组件A
      <span class="hljs-tag"><<span class="hljs-name">br</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setVisible(v => !v)&#125;
        onMouseEnter=&#123;() => !visible && revalidate()&#125;
      >
        点我-&#123;!visible ? "显示" : "隐藏"&#125;组件B
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#123;visible && <span class="hljs-tag"><<span class="hljs-name">CompB</span> /></span>&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useData()
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件B：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中执行 <code>revalidate()</code> 后就会发起请求，获取数据，实现预加载。以上代码有两点值得提出来分析下。</p>
<ol>
<li>在组件 A 中调用 useData 时传参是 false，因为不希望挂载组件 A 时产生不必要的请求，避免导致页面需要的请求延后。</li>
<li>展示组件 B 时，组件 A 中已经发起了预加载请求，按理来说我们应该在组件 B 中调用 useData 时也传参 false。但是我们没有这样做，我们从预加载请求的状态来分析下原因。1.) 如果预加载的请求还在进行中，且不超过 dedupingInterval，那么挂载时就不会发起新的请求。2.) 如果预加载请求已结束，再发一次请求也不占用资源，而且还提升了组件 B 在不需要预加载的场景下的复用性。</li>
</ol>
<p>如果没这么讲究，可以直接组件 A 中调用 <code>useData()</code> 或在组件 A 中挂载组件 B，但用 <code><div style=&#123;&#123; display: 'none' &#125;&#125;></code> 隐藏组件 B。这两种方式的缺点都是，在挂载组件 A 时会发出与当前页面无关的请求，占用资源。通过 <code>display: 'none'</code> 实现时，如果组件 B 的 Render 过程很费时，还会导致性能问题，影响首屏渲染。举个例子，在分页场景中，将分页展示数据封装为 Page 组件，则我们可以非常简单地实现下一页的数据预加载。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 分页场景下，预加载下一页数据</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Page</span>(<span class="hljs-params">&#123; index &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR(<span class="hljs-string">`/api/data?page=<span class="hljs-subst">$&#123;index&#125;</span>`</span>, fetcher)

  <span class="hljs-comment">// ... 处理加载和错误状态</span>

  <span class="hljs-keyword">return</span> data.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span>&#123;item.name&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
&#125;

<span class="hljs-comment">// 方式一：通过直接调用 useSWR()，获取下一页数据</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [page, setPage] = useState(<span class="hljs-number">0</span>)
  <span class="hljs-comment">// 预加载下一页数据</span>
  useSWR(<span class="hljs-string">`/api/data?page=<span class="hljs-subst">$&#123;page + <span class="hljs-number">1</span>&#125;</span>`</span>, fetcher)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Page</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;page&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setPage(page - 1)&#125;>上一页<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setPage(page + 1)&#125;>下一页<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-comment">// 方式二：通过 display: "none" 实现</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [page, setPage] = useState(<span class="hljs-number">0</span>)

  <span class="hljs-comment">// 将 <Page index=&#123;pageIndex + 1&#125; /> 放在最后面</span>
  <span class="hljs-comment">// 尽量避免阻塞当前页面需要的请求</span>
  <span class="hljs-comment">// 这种方式不适合 Page 组件很复杂的场景，会导致性能问题。</span>
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Page</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;page&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setPage(page - 1)&#125;>上一页<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setPage(page + 1)&#125;>下一页<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> "<span class="hljs-attr">none</span>" &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Page</span> <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;pageIndex</span> + <span class="hljs-attr">1</span>&#125; /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，<a href="https://useswr.vercel.app/docs/prefetching#programmatically-prefetch" target="_blank" rel="nofollow noopener noreferrer">官网推荐的预加载方式</a>是使用 mutate 实现。但使用 mutate 实现时，需要导出 <code>useData</code> 的同时导出 key 和 fetcher 给 CompA 使用，写起来会麻烦一些。</p>
<h2 data-id="heading-10">5. 组件卸载后不执行 setState</h2>
<p>当 React 组件中带有数据请求时，如果组件在请求结果返回前被卸载了，React 会警告我们组件存在内存泄漏问题。</p>
<p><img alt="React Warning-组件卸载后执行 setState.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d534b5c5ba7e45eeb13dc82e7788d999~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为了避免这个警告，我们在实现组件时，会使用 unmountedRef 标记组件是否卸载，如果组件已经被卸载了就不执行状态更新语句。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState()
  <span class="hljs-keyword">const</span> unmountedRef = useRef(<span class="hljs-literal">false</span>)
  useEffect(<span class="hljs-function">() =></span> &#123;
    ;(<span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">2000</span>))
      <span class="hljs-keyword">if</span> (!unmountedRef.current) &#123;
        <span class="hljs-comment">// 如果组件已经被卸载了，仍执行 setData</span>
        <span class="hljs-comment">// React 会报出 Warning 警告</span>
        setData(<span class="hljs-string">"MoonBall"</span>)
      &#125;
    &#125;)()

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      unmountedRef.current = <span class="hljs-literal">true</span>
    &#125;
  &#125;, [])
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>data: &#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 useSWR 后，我们完全不用关心该问题，因为它会在组件卸载后将状态更新函数修改为 noop，参考<a href="https://github.com/vercel/swr/blob/fa676db47512b07b539e8b933932d714a2e5d3b3/src/use-swr.ts#L647" target="_blank" rel="nofollow noopener noreferrer">源码</a>。这个技巧比较巧妙，上面的例子如果运用该技巧，代码就会更简洁。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState()
  <span class="hljs-keyword">let</span> dispatch = setData
  useEffect(<span class="hljs-function">() =></span> &#123;
    ;(<span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">2000</span>))
      <span class="hljs-comment">// 如果组件已经被卸载了，dispatch 就是空函数，</span>
      <span class="hljs-comment">// 不会触发 React 警告</span>
      dispatch(<span class="hljs-string">"MoonBall"</span>)
    &#125;)()

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      dispatch = <span class="hljs-function">() =></span> &#123;&#125;
    &#125;
  &#125;, [])
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>data: &#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">5. 其他</h2>
<p>其他主要包括轮询机制、错误重试机制和 focus/online 重试机制。这些机制在业务上虽然使用得不多，但需要的时候自己实现还是会比较麻烦。</p>
<h1 data-id="heading-12">useSWR 的缺点</h1>
<h2 data-id="heading-13">全局 key 命名问题</h2>
<p>跟 Redux 中的 ActionType 一样，都是全局命名问题。</p>
<h2 data-id="heading-14">未提供请求中断的 API</h2>
<p>在<a href="https://juejin.cn/post/6942281123317678087#heading-7">请求时序问题</a>中，请求 2 发出时如果请求 1 没有结束，最好的处理方式是将请求 1 进行终止，避免资源浪费，类似 <a href="https://github.com/axios/axios#cancellation" target="_blank" rel="nofollow noopener noreferrer">axios 的取消机制</a>。可惜目前 useSWR 并没有提供终止请求的方法。</p>
<h2 data-id="heading-15">没有 getter 方法去读取数据</h2>
<p>useSWR 只有通过它提供的 Hook 才能访问到数据，没有提供一个 getter 方法通过 key 获取数据。这在复杂的更新逻辑中还是很需要的，类似于 Redux 的 getState 方法，在任何地方需要某个全局数据时，调一下就拿到数据的当前值了，非常方便。而 useSWR 只通过 Hook 返回请求的数据，需要从页面一直传到需要该数据的地方，非常麻烦。</p>
<h2 data-id="heading-16">配置相对于 key 还是相对于 Hook 的，傻傻分不清</h2>
<p>useSWR 中请求是相对于 key 的，但 fetcher 和配置却是相对于 Hook 的，比如同 key 的 useSWR 是可以使用不同的 fetcher 和配置的。尽管我们不会那样写，但还是会造成理解负担。关于这点我们可通过<a href="https://juejin.cn/post/6942281123317678087#heading-19">最佳实践-代码组织</a>来避免，保证相同 key 的请求的 fetcher 和 config 是一致的。</p>
<p>这种设计就存在一个无法修复的 bug，当调用 useSWR 是传了 initialData，那么使用 mutate 时，并不会将当前的 data 传给 mutate 的回调。其原因就是因为 mutate 中的 data 是相对于 key 的，而 initialData 却是相对于 Hook 的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 传了 initialData 后，第一次调用 mutate 时，回调函数的 data 是 undefined</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Comp</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, mutate &#125; = useSWR(<span class="hljs-string">"api/data"</span>, fetcher, &#123;
    <span class="hljs-attr">initialData</span>: <span class="hljs-string">"MoonBall"</span>,
  &#125;)

  <span class="hljs-keyword">const</span> handleChange = <span class="hljs-function">() =></span> &#123;
    mutate(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-comment">// 第一次调用时这里的 data 是 undefined</span>
      <span class="hljs-comment">// 所以会报错</span>
      <span class="hljs-keyword">return</span> data.slice(<span class="hljs-number">0</span>, <span class="hljs-number">4</span>)
    &#125;)
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleChange&#125;</span>></span>修改<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      data: &#123;data&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">需要手动删除不使用的缓存，避免内存泄漏</h2>
<p>目前所有 key 对应的响应结果都没有被删除，为了避免内存泄漏，需要开发人员主动清理缓存，可参考<a href="https://juejin.cn/post/6942281123317678087#heading-21">最佳实践-清理 Cache 避免内存泄漏</a>。</p>
<h1 data-id="heading-18">最佳实践</h1>
<h2 data-id="heading-19">代码组织</h2>
<p>将使用 useSWR 请求的代码提取为单独的 Hook，以便多个组件进行复用，像前面实现的 useData 一样。如果将同 key 的请求放在不同的位置，就可能导致各个地方给 useSWR 调用时传的 fetcher 和 config 不同，导致莫名其妙的问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 不推荐将同 key 的请求分散到各处</span>
<span class="hljs-comment">// 比如下面两个 fetcher 函数的返回值就不同</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR(<span class="hljs-string">"/api/data"</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
    <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall"</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件A：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CompB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data &#125; = useSWR(<span class="hljs-string">"/api/data"</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">500</span>))
    <span class="hljs-keyword">return</span> <span class="hljs-string">"MoonBall-2"</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>组件B：&#123;data || "-"&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">Error 处理</h2>
<p>在前面我们实现的 <code>useFetch</code> 方法中，每次请求出错都会执行 <code>throw err</code> 将错误再抛出去。但 useSWR 中并没有这样做，它将错误吃掉了，并通过 onError 反馈给我们。所以我们一定要设置全局的 onError 回调函数，并打印 err 或将 err 上传至 Sentry，方便我们定位问题。</p>
<h2 data-id="heading-21">清理 Cache 避免内存泄漏</h2>
<p>前面说到 useSWR 不会自动清理请求响应，所以我们需要主动清理缓存，避免内存泄漏。在 SPA 应用中，建议在页面组件卸载时执行 <code>cache.clear()</code> 来清理缓存。但整个应用中某些接口是跨页面共享的，属于应用级别的数据，它们不应该被清理掉，比如用户信息，应用版本配置等等。还好这些跨页面应用级别的接口并不多，这些接口仍然可通过 Redux 等其他状态管理库实现，只有页面内的接口才使用 useSWR 实现。</p>
<p>在页面组件中调用如下 Hook 就可以将缓存清理掉，避免内存泄漏。</p>
<pre><code class="copyable">import &#123; cache &#125; from "useSWR";

function useCacheClearWhenPageUnmount() &#123;
  return useEffect(() => &#123;
    return () => &#123;
      cache.clear();
    &#125;;
  &#125;, []);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前<a href="https://github.com/vercel/useSWR/pull/1017" target="_blank" rel="nofollow noopener noreferrer">自定义 Cache 的 PR</a> 正在进行中，未来我们可以通过自定义 Cache 来避免内存泄漏问题。</p>
<h1 data-id="heading-22">总结</h1>
<p>本文给大家分享了 useSWR 的设计思想、使用场景和最佳实践，相信 useSWR 一定会提升大家的编码效率、代码简洁性和可读性。</p>
<p>后续我也计划分享 React Query，并将它和 SWR 进行对比，敬请期待。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            