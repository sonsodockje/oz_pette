import { createTheme } from '@mui/material/styles'

const theme = createTheme({
    palette: {
        common: {
            customWhite: '#ffffff',
            customYellow: '#ffc145',
            customRed: '#ff6b6c',
            customPurple: '#b8b8d1',
            customBlack: '#48495c',
            customGray: '#a7a7a7',
        },
    },
    typography: {
        fontSize: {
            xs: 16, // 모바일
            md: 20, // 태블릿
            lg: 24, // 데스크톱
        },
    },
})

export default theme
