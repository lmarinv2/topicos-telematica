const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // devServer: {
  //   proxy: {
  //     '/api': {
  //       target: 'http://localhost:8000',
  //       ws: true,
  //       changeOrigin: true
  //     }
  //   }
  // }
  devServer: {
      proxy: {
        "/api": {
          target: "http://127.0.0.1:8000",
          secure: false,
          changeOrigin: true,
          ws: true
        }
      }
    }
})
